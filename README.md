# Temporal Fusion Transformer 알고리즘을 SageMaker 에서 분산 훈련 하기

# 1. 배경 및 주요 내용
Temporal Fusion Transformer 알고리즘은 SOTA 를 기록할 만큼 트랜서포머를 기반으로 포케스팅에서 최근에 많이 사용하는 알고리즘 입니다.

[Demand forecasting with the Temporal Fusion Transformer](https://pytorch-forecasting.readthedocs.io/en/stable/tutorials/stallion.html) 의 예제 코드를 실행하면 모델 훈련 부터 추론까지 할 수 있습니다. 이 코드에서 "모델 훈련" 부분만을 여러가지 아래의 방법으로 모델 훈련 합니다. 

- PyTorch Lightning 의 기본 내장된 Multi-GPUs 모델 학습을 합니다.
    - 1_Training/1.1.Run_TFT_DT_Local.ipynb
- 세이지 메이커의 훈련 잡을 이용하여 PyTorch Lightning 의 기본 내장된 Multi-GPUs 모델 학습을 합니다. 로컬 모드를 실행한 후에 클라우드 모드로 모델 훈련 합니다.
    - 1_Training/2.1.Run_TFT_DT_SageMaker.ipynb
- 세이지 메이커의 훈련 잡을 이용하여 2개의 머신에서 [SageMaker DDP](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp-pt-lightning.html) 를 이용하여 학습합니다. 로컬 모드를 실행한 후에 클라우드 모드에서 2개의 머신으로 모델 훈련 합니다.
    - 1_Training/3.1.Scripts2_.Run_TFT_DT_SageMaker_DDP.ipynb

# 2. 실행 방법
## 2.1 선수 조건
- 이 리포는 세이지 메이커 노트북 인스턴스의 ml.p3.2xlarge, ml.p3.16xlarge 에서 테스트 되었습니다. 싨습시에 GPU 기반의 세이지 메이커 노트북 인스턴스에서 실행하시기 바랍니다.

## 2.2 실행 순서
- 아래의 환경 셋업 노트북을 실행 합니다. 
    - 0_Setup/1.1.Setup_Environment.ipynb
- 아래의 3개의 노트북을 순서대로 실행 합니다.  
    - 1_Training/1.1.Run_TFT_DT_Local.ipynb
    - 1_Training/2.1.Run_TFT_DT_SageMaker.ipynb    
    - 1_Training/3.1.Scripts2_.Run_TFT_DT_SageMaker_DDP.ipynb    

# A. 참조
- Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting
    - https://arxiv.org/abs/1912.09363
- PyTorch Forecasting
    - https://github.com/jdb78/pytorch-forecasting
- PyTorch Lightning
    - https://pytorch-lightning.readthedocs.io/en/latest/
- SageMaker에서 PyTorch Lightning 분산 훈련 실습
    - https://www.youtube.com/watch?v=ZCbfyPPdmS4
- Modify a PyTorch Lightning Script
    - https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-modify-sdp-pt-lightning.html
- Probabilistic Time Series Forecasting with 🤗 Transformers
    - https://huggingface.co/blog/time-series-transformers
- Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting implemented in Pytorch (파이토치 버전)
    - https://github.com/dehoyosb/temporal_fusion_transformer_pytorch