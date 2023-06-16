# 커리큘럼 . 



| 회차                                                         | 학습 내용                                                    |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1회차                                                        | **강의 내용 소개 및 텍스트 마이닝 프레임워크**: 텍스트 마이닝 기본 요소들의 정의와 document classification의 핵심 요소를 살펴봅니다. |                                                              |
| - KoNLPy를 이용하여 문서 집합을 토크나이징합니다. - 텍스트 분석 시 발생하는 '미등록단어' 문제를 알아봅니다. - Bag-of-Words Model과 n-gram을 알아봅니다. - Document Classification에 대표적으로 이용되는 Logistic Regression에 대하여 알아봅니다. - KoNLPy와 Logistic Regression을 이용하여 영화평 분류기를 만들어 봅니다. |                                                              |                                                              |
| 2~3회차                                                      | **한국어 자연어 처리 모듈 개발**: 지도학습과 비지도학습으로 품사 판별기와 형태소 분석기를 만듭니다. | **키워드 및 연관어 분석**: 데이터를 기반으로 수행되는 키워드와 연관어를 추출합니다. |
| - 사전 구축 및 비지도학습 기반 품사 판별기/ 형태소 분석기 > 미등록단어 문제를 해결하기 위한 비지도학습 기반 단어 추출 방법과 토크나이저를 알아봅니다. > 통계 기반으로 단어의 품사(특히 명사)를 추정하는 방법을 살펴보고, 이를 이용하여 학습 데이터에 존재하지 않는 단어/품사 사전을 구축합니다. > 구축된 사전을 이용하여 사전 기반 자연어 처리 모듈을 만듭니다.  - 학습 말뭉치 기법 지도학습 품사 판별기/ 형태소 분석기 > 자연어 처리를 위하여 이용되던 HMM(Hidden Markov Model)을 알아봅니다.  - HMM을 이용한 지도학습 기반 자연어 처리 모듈을 만듭니다. | - 연관성을 수치화 하는 PMI(Pointwise Mutual Information)를 알아보고, 이를 이용하여 연관어/ 키워드를 추출합니다. - Logistic Regression에 L1 Regularization을 추가하여 연관어/ 키워드를 추출합니다. |                                                              |
| 4회차                                                        | **Document Classification**: 분류 모델(classifiers)을 알아보고, 텍스트 데이터에 적합한 분류기와 그 이유를 알아봅니다. | **Sequential Labeling을 위한 CRF(Conditional Random Field)** |
| - Feed-forward Neural Network, SVM(Support Vector Machine), Decision Tree, Naive Bayes의 작동 원리를 알아봅니다. | - CRF의 작동 원리와 함께, CRF와 Logistic Regression의 관계를 살펴봅니다. - CRF를 이용하여 띄어쓰기 교정기를 만듭니다. - CRF를 이용하여 HMM보다 성능이 좋은 한국어 자연어 처리 모듈을 만듭니다. - CRF를 이용하여 NER(Named Entity Recognition)을 수행합니다. |                                                              |
| 5회차                                                        | **Word/ Document Embedding**: 단어와 문서를 표현하는 방식인 임베딩에 대하여 알아봅니다. | **Embedding for Visualization**: 고차원 벡터를 시각화하기 위한 임베딩 방법에 대하여 알아봅니다. |
| - 대표적인 Word Embedding 방법인 Word2Vec, Glove, FastText의 원리 및 공통점/ 차이점을 알아봅니다. - 대표적인 Document Embedding 방법인 Doc2Vec의 원리를 알아봅니다. | - 시각화를 위하여 이용되는 다음의 알고리즘의 원리 및 공통점/ 차이점과 함께, Word/ Document Embedding 시각화에 적합한 알고리즘도 알아봅니다. > MDS(Multi-Dimensional Scaling) > PCA(Principal Component Analysis)/ kPCA(kernel-PCA) > LLE(Locally Linear Embedding) > ISOMAP > t-SNE(t-Stochastic Neighbor Embedding) |                                                              |
| 6회차                                                        | **Topic Modeling**: 문서 집합으로부터 숨겨진 토픽을 학습하는 토픽 모델링에 대하여 알아봅니다. |                                                              |
| - LSI(Latent Semantic Indexing), pLSI(Probabilistic LSI), LDA(Latent Dirichlet Allocation)으로의 토픽 모델링 발전 과정을 알아봅니다. - pyLDAvis를 이용한 토픽 모델링 시각화 방법과 토픽 레이블링 방법을 알아봅니다. - 토픽 모델링에 이용될 수 있는 다른 방법론인 Sparse Coding, NMF(Non-negative Matric Factorization)에 대해서도 알아봅니다. |                                                              |                                                              |
| 7회차                                                        | **Document Clustering**: 비슷한 문서를 하나의 집합으로 묶는 문서 군집화 방법들을 알아봅니다. | **Vector Indexing**: 벡터로 표현된 대량의 데이터로부터 유사한 벡터를 빠르게 찾는 방법을 알아봅니다. |
| - (Spherical) k-means, Hierarchical Clustering과 그 외 문서 군집화 방법들의 특징을 알아봅니다. - k-means가 왜 다른 알고리즘보다 문서 군집화에 적합한지 살펴봅니다. - k-means를 효율적으로 학습하는 방법과 데이터 기반으로 군집 레이블링 하는 방법을 살펴봅니다. | - Random Projection을 이용하는 LSH(Locality Sensitive Hashing)의 원리를 알아봅니다. - Sparse Representation으로 표현되는 문서 검색을 위한 Inverted Index(역 색인)를 알아봅니다. |                                                              |
| 8회차                                                        | **String Distance**: 글자열의 형태적 유사성 척도인 String Distance에 대하여 알아봅니다. | **Graph Ranking/ Similatiry**: 텍스트 데이터를 그래프로 표현하는 방법에 대하여 알아봅니다. |
| - Levenshtein (Edit) Distance의 원리를 알아보고, 한국어 오탈자 교정에 적합하도록 이를 변형합니다. -기타 String Distance Metrics에 대해서도 알아봅니다. - Inverted Index를 이용하여 빠르게 Levenshtein Distance를 계산하는 오탈자 교정기를 만듭니다. | - 키워드/ 핵심 문장 주출을 위한 Graph Ranking 알고리즘인 PageRank, HITS를 알아봅니다. - Graph Ranking 알고리즘을 이용하여 단어를 추출하는 TextRank, KR-WordRank를 살펴봅니다. - 의미적으로 비슷한 단어/ 문서를 검색할 수 있는 Graph Similarity 방법론인 SimRank, Random Walk with Restart를 알아봅니다. |                                                              |
| 9회차                                                        | **PyTorch**                                                  | **CNN(Convolutional Neural Network)**                        |
| - Deep Learning Modeling을 위한 PyTorch의 기본 요소들을 알아보고, Classifier 및 Regressor를 만들어 봅니다. | - CNN 모델의 원리에 대하여 살펴봅니다. - NLP를 위한 대표적인 CNN 모델인 Word-level CNN과 Character-level CNN을 알아봅니다. |                                                              |
| 10회차                                                       | **RNN(Recurrent Neural Network)**                            |                                                              |
| - RNN 모델의 원리에 대하여 살펴봅니다. - NLP를 위한 RNN의 발전 모델인 LSTM, GRU, Attention을 살펴봅니다. - 최근의 자연어 처리 연구 동향을 살펴봅니다. |                                                              |                                                              |



[강의 summary 보러 가기 ](https://cdn.www.fastcampus.co.kr/wp-content/uploads/2018/12/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%9E%90%EC%97%B0%EC%96%B4-%EC%B2%98%EB%A6%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-CAMP_summary.pdf)







#### 강의 자료 예시



![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/bfi_thumb/nlp1-o00z04v40lh25tuozk33oqrlc64ugoznvhioe8tvia.png)

![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/bfi_thumb/nlp2-o00z0bfzcfq2f3l4x4xho73thv8eykps8e32r6k4aq.png)

![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/bfi_thumb/nlp3-o00z0i0uo9z2odbkuprvnng1nkbzggfwlanh44ad36.png)



- 
- 

![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/bfi_thumb/nlp4-o00z0ls7fm47yt648redxmhw13tgb8utxt9f184sea.png)

![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/bfi_thumb/nlp5-o00z0sd2rgd882wk6c8rx2u46sx0t4kyaptte5v16q.png)

![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/bfi_thumb/nlp6-o00z0x29pmjnu4pqew9wrjnf5q9uvm3lzd38sjo2bm.png)

![img](https://cdn.www.fastcampus.co.kr/wp-content/uploads/bfi_thumb/nlp7-o00z11rgnsq3g6iwngb1m0gq4nmoy3m9o0co6xh3gi.png)



- 
- 