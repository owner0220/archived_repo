#  커리큘럼**.**





\* 실습은 AWS 서버에 접속해서 진행됩니다. 따라서 개인 노트북 사양은 크게 중요하지 않습니다.
\* 각 회차별로 진행되는 주요 실습에 대한 예시 이미지가 있으니, 참고해주기 바랍니다.



![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/2018/09/process2-02.png)

#### PART 1. PYTORCH & DEEP LEARNING BASIC



#### 1회차 : DEEP LEARNING & PYTORCH: 딥러닝이란 무엇인가 알아보고, 왜 PYTORCH를 배워하는지 개념을 다집니다.



**Introduction**
\> 왜 딥러닝인가?
\> 왜 PyTorch인가?

**PyTorch Basic**
\> PyTorch 설치 및 환경 구축
\> PyTorch Tensor 다루기

[실습] Python Basic
[실습] PyTorch 4.0

#### 2회차 :BASICS FOR MODEL TRAINING: 모델 학습을 이해하면서 PYTORCH를 통해 회귀/분류 모델을 구현해 봅니다.



**Model Training**
\> Supervised & Unsupervised Learning
\> Model Training Process
\> Loss Function/ Gradient Descent/ Backpropagation

**Regression Models**
\> Linear Regression
\> Multivariate Linear Regression

**Classification Models**
\> Logistic Regression

[실습] Linear Regression
[실습] Multivariate Linear Model
[실습] Logistic Regression

#### PART 2. NEURAL NETWORK & CONVOLUTIONAL NEURAL NETWORK

#### 3회차 : NN & CNN: 딥러닝의 기초가 되는 NN(NEURAL NETWORK)을 배워보고, 다양한 데이터에 적용해 봅니다. 더 나아가 이미지 데이터를 다루기 위한 CNN을 활용해 봅니다. 



Neural Networks
> Activation Functions
> Neural Network
> MNIST
> Batch Training

CNN
> Convolution Layer
> Pooling Layer
> Fully Connected Layer
> GRAY/ RGB

[실습] Activation Functions
[실습] Neural Networks
[실습] Neural Network with MNIST
[실습] CNN with MNIST
[실습] Simple CNN with HANGUL JAMO

#### 4회차 : METHOD FOR IMPROVING MODELS: 기존 모델들의 성능 한계를 확인하고, 이를 극복하기 위해 뛰어난 성능을 보였던 CNN 모델들의 특징과 구조를 익혀 분석해 봅니다.



Methods for Improving Model
> Data Preprocessing
> Other Optimizers
> Weight Initialization/ Regularization
> Batch Normalization/ Dropout

**Advanced CNN**
\> AlexNet/ VGGNet
\> GoogLeNet/ ResNet
\> Inception

**Transfer Learning**
\> Feature Extraction
\> Fine Tuning

[실습] Improving Simple CNN
[실습] CNN with CIFAR10
[실습] Feature Extraction with VGG16
[실습] Transfer Learning with Inception v3

#### PART 3. NATURAL LANGUAGE PROCESSING & RECURRENT NEURAL NETWORK

#### 5회차 : NLP(NATURAL LANGUAGE PROCESSING): SNS, 리뷰, 기사 등 자연어 분석을 위한 방법을 익히고, 실제 리뷰 데이터를 기반으로 감성 분석을 진행해 봅니다.



**Preprocessing with Natural Language**
\> Tokenize/ Stopping
\> Stemming/ POS-tagging
\> N-gram

**Bag of Words**
\> TF-IDF

**Word2Vec**
\> Skip-Gram
\> CBOW

**Sentimental Analysis**

[실습] NLTK & Konlpy
[실습] Sentimental Analysis with Bag of Words and NN
[실습] Sentimental Analysis with Word2Vec and CNN

#### 6회차 : RNN(RECURRENT NEURAL NETWORK): SEQUENTIAL 데이터를 분석하기 위한 기법인 RNN을 익힙니다. 또한 앞서 학습한 자연어 처리 기법을 적용하여 셰익스피어의 문체를 모방하고, 시계열 데이터인 가상화폐 가격을 예측해 봅니다.



**Sequential Data**
**RNN**
**GRU(Gated Recurrent Unit)**
**LSTM (Long Short-Term Memory Models)**

[실습] RNN with Bag of Words & Hamlet
[실습] LSTM with Word2Vec & Moby Dick
[실습] RNN for Cryptocurrency Price Predicting

#### PART 4. AUTO-ENCODER & GENERATIVE ADVERSARIAL NETWORKS

#### 7회차 : AUTO-ENCODER: 이미지의 특성을 추출하여 이미지를 재구성하는 GENERATIVE MODEL 구현을 위한 AUTO-ENCODER를 익힙니다. 또한 DENOISING 기법을 통해 이미지의 노이즈를 제거해 봅니다.



**Auto-Encoders**
**Convolutional Auto-Encoders**
**VAE(Variational Auto-Encoders)**
**Denoising Auto-Encoders**

[실습] Standard Auto-Encoder
[실습] Convolutional Auto-Encode
[실습] Variational Auto-Encoder
[실습] Denoising Auto-Encoder

#### 8회차 : GAN(GENERATIVE ADVERSARIAL NETWORKS): GENERATIVE MODEL의 강자인 GAN을 통해 생성 모델의 무한한 가능성을 확인해 봅니다.



**GAN**
**DCGAN(Deep Convolutional Generative Adversarial Networks)**
**cGAN(Conditional GAN)**
\> Pix2Pix

**Recent Works**
\> InfoGAN
\> Progressive GAN

[실습] GAN
[실습] DCGAN
[실습] cGAN
[실습] Pix2Pix



# 강의 실습 예시**.**



\1. 간편한 데이터 처리: Python을 알고 있다면 이해할 수 있는 코드로 쉽게 데이터를 처리할 수 있습니다.



![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/2018/12/pt_1-1024x461.png)

\2. 직관적인 모델링: 아래 슬라이드에서 Linear(64*3*3, 100)을 활용한다고 설명된 것처럼, 딥러닝의 개념을 코드에 그대로 적용 가능합니다.



![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/2018/12/pt_2-1024x461.png)

\3. 편한 오류 수정 및 디버깅: 코드 실행 단계에서 중간중간 결과 확인이 되어, 어디에서 오류가 있는지 빠르게 파악 가능합니다.



![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/2018/12/pt_3-1024x461.png)

\4. 빠른 모델 검증 및 확인: 간결한 코드로 모델의 정확도를 검증할 수 있습니다.



![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/2018/12/pt_4-1024x277.png)