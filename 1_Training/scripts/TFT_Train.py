print("######################")
print("######## TEST #########")
print("######################")
import os
import warnings

warnings.filterwarnings("ignore")  # avoid printing out absolute paths

import copy
from pathlib import Path
import warnings

import numpy as np
import pandas as pd
import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping, LearningRateMonitor
from pytorch_lightning.loggers import TensorBoardLogger
import torch

from pytorch_forecasting import Baseline, TemporalFusionTransformer, TimeSeriesDataSet
from pytorch_forecasting.data import GroupNormalizer
from pytorch_forecasting.metrics import SMAPE, PoissonLoss, QuantileLoss
from pytorch_forecasting.models.temporal_fusion_transformer.tuning import optimize_hyperparameters
from pytorch_forecasting.data.examples import get_stallion_data    


import argparse

def train(args):
    data = get_stallion_data()

    # add time index
    data["time_idx"] = data["date"].dt.year * 12 + data["date"].dt.month
    data["time_idx"] -= data["time_idx"].min()

    # add additional features
    data["month"] = data.date.dt.month.astype(str).astype("category")  # categories have be strings
    data["log_volume"] = np.log(data.volume + 1e-8)
    data["avg_volume_by_sku"] = data.groupby(["time_idx", "sku"], observed=True).volume.transform("mean")
    data["avg_volume_by_agency"] = data.groupby(["time_idx", "agency"], observed=True).volume.transform("mean")

    # we want to encode special days as one variable and thus need to first reverse one-hot encoding
    special_days = [
        "easter_day",
        "good_friday",
        "new_year",
        "christmas",
        "labor_day",
        "independence_day",
        "revolution_day_memorial",
        "regional_games",
        "fifa_u_17_world_cup",
        "football_gold_cup",
        "beer_capital",
        "music_fest",
    ]
    data[special_days] = data[special_days].apply(lambda x: x.map({0: "-", 1: x.name})).astype("category")
    # data.sample(10, random_state=521)
    
    max_prediction_length = 6
    max_encoder_length = 24
    training_cutoff = data["time_idx"].max() - max_prediction_length

    training = TimeSeriesDataSet(
        data[lambda x: x.time_idx <= training_cutoff],
        time_idx="time_idx",
        target="volume",
        group_ids=["agency", "sku"],
        min_encoder_length=max_encoder_length // 2,  # keep encoder length long (as it is in the validation set)
        max_encoder_length=max_encoder_length,
        min_prediction_length=1,
        max_prediction_length=max_prediction_length,
        static_categoricals=["agency", "sku"],
        static_reals=["avg_population_2017", "avg_yearly_household_income_2017"],
        time_varying_known_categoricals=["special_days", "month"],
        variable_groups={"special_days": special_days},  # group of categorical variables can be treated as one variable
        time_varying_known_reals=["time_idx", "price_regular", "discount_in_percent"],
        time_varying_unknown_categoricals=[],
        time_varying_unknown_reals=[
            "volume",
            "log_volume",
            "industry_volume",
            "soda_volume",
            "avg_max_temp",
            "avg_volume_by_agency",
            "avg_volume_by_sku",
        ],
        target_normalizer=GroupNormalizer(
            groups=["agency", "sku"], transformation="softplus"
        ),  # use softplus and normalize by group
        add_relative_time_idx=True,
        add_target_scales=True,
        add_encoder_length=True,
    )
    # create validation set (predict=True) which means to predict the last max_prediction_length points in time
    # for each series
    validation = TimeSeriesDataSet.from_dataset(training, data, predict=True, stop_randomization=True)

    # create dataloaders for model
    batch_size = 128  # set this between 32 to 128
    train_dataloader = training.to_dataloader(train=True, batch_size=batch_size, num_workers=0)
    val_dataloader = validation.to_dataloader(train=False, batch_size=batch_size * 10, num_workers=0)
    
    ##################
    # Train
    #################
    
        # configure network and trainer
    early_stop_callback = EarlyStopping(monitor="val_loss", min_delta=1e-4, patience=10, verbose=False, mode="min")
    lr_logger = LearningRateMonitor()  # log the learning rate
    logger = TensorBoardLogger("lightning_logs")  # logging results to a tensorboard

    trainer = pl.Trainer(
        max_epochs=args.epochs,
        gpus = args.n_gpus,        
        accelerator='cuda',
        enable_model_summary=True,
        gradient_clip_val=0.1,
        callbacks=[lr_logger, early_stop_callback],
        logger=logger,
    )


    tft = TemporalFusionTransformer.from_dataset(
        training,
        learning_rate=0.03,
        hidden_size=16,
        attention_head_size=1,
        dropout=0.1,
        hidden_continuous_size=8,
        output_size=7,  # 7 quantiles by default
        loss=QuantileLoss(),
        log_interval=10,  # uncomment for learning rate finder and otherwise, e.g. to 10 for logging every 10 batches
        reduce_on_plateau_patience=4,
    )
    print(f"Number of parameters in network: {tft.size()/1e3:.1f}k")


    # fit network
    trainer.fit(
        tft,
        train_dataloaders=train_dataloader,
        val_dataloaders=val_dataloader,
    )
    
    chk_path = os.path.join(args.model_dir, 'model.pth')
    trainer.save_checkpoint(chk_path)
    
    
def parser_args(train_notebook=False):
    parser = argparse.ArgumentParser()

    # Default Setting
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--seed", type=int, default=100)
    parser.add_argument("--train_batch_size", type=int, default=64)

    # SageMaker Container environment
    parser.add_argument("--model_dir", type=str, default=os.environ["SM_MODEL_DIR"])
    parser.add_argument("--n_gpus", type=str, default=os.environ["SM_NUM_GPUS"])
    # parser.add_argument("--training_dir", type=str, default=os.environ["SM_CHANNEL_TRAIN"])
    # parser.add_argument("--test_dir", type=str, default=os.environ["SM_CHANNEL_TEST"])

    if train_notebook:
        args = parser.parse_args([])
    else:
        print("Not running on notebook")
        args = parser.parse_args()
    return args
    
    
if __name__ == '__main__':
    args = parser_args()    
    print("***** Arguments *****")
    print(''.join(f'{k}={v}\n' for k, v in vars(args).items()))
    
    train(args)


