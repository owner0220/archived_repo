## 커리큘럼.





| 주차                                                         | 내용                          |
| ------------------------------------------------------------ | ----------------------------- |
| Part 1. Apache Spark, 꼭 알아야할 핵심 개념                  |                               |
| 1-3                                                          | Apache Spark 이해하기         |
| Apache Spark의 정의와 특징을 살펴보고 그 작동원리를 이해합니다. Apache Spark에서 사용하는 Scala 언어의 특징을 알아보고 기본적인 사용법을 배웁니다. Apache Spark 실습진행을 위해 필요한 설치 및 환경설정을 합니다.  - Spark 개요(Apache Spark 소개, 특징, 지원언어, Hadoop과 비교, Spark 프로그래밍 모델(RDD), 작동원리, Spark Components 등) - Scala 개요(Scala 언어 소개, 특징, 변수 선언, 함수 정의 등 기본 문법) - Spark 설치 및 실행(VirtualBox, CentOS7, Java 8, Spark 설치 및 환경설정, 프로세스, Lineage 확인 등 Spark Shell 기본 사용법) |                               |
| Spark Core                                                   |                               |
| Spark Core Components 각각의 기능을 살펴보고, 분산환경(클러스터) 설정과 함께 RDD Operation을 이해합니다. RDD 생성부터 Transform까지 RDD 프로그래밍을 해봅니다.  병렬 수행되는 클러스터상의 Task를 위한 Shared Variables에 대해 배웁니다.  - Spark RDD 개요(Spark Core Components, Spark Application 배포, RDD Operations 등) - RDD 프로그래밍(RDD 생성, RDD Transform, RDD Action 등) - Shared Variables(Broadcast, Accumulators) |                               |
| Part 2. Apache Spark의 다양한 라이브러리 정복하기            |                               |
| 4-10                                                         | Spark SQL                     |
| Spark 기반으로 SQL을 사용하기 위해 필요한 기본개념과 DataFrame/Dataset, Catalyst Optimizer에 대해 배웁니다.  - Spark SQL 개요(특징, 성능, RDD와 DataFrame/Dataset의 비교, SparkSession) - DataFrame/Dataset(생성법, Basic Operations, Queries, Join, 저장, Row Object 처리 등) - Catalyst Optimizer 및 Tungsten Project 작동원리 |                               |
| Spark Streaming                                              |                               |
| 실시간으로 스트림 데이터를 빠르게 처리하는 Spark Streaming과 Structured Streaming을 배웁니다.  - Spark Streaming(특징 및 기능, DStream의 개념 및 Basic Operations, Stateful Operations, Execution Model, DStream Persistence, Checkpoint, Kafka 연계 등) - Structured Streaming(DStream의 문제점, Programming Model, Window Operations, Watermarking 등) - 실습 데이터 : twitter를 이용하여 SNS 데이터 수집 |                               |
| Spark ML                                                     |                               |
| Spark ML의 특징을 살펴보고, 사용가능한 알고리즘들을 알아봅니다.다양한 모델을 구축하고 테스트하는 방법에 대해 배웁니다.  - Spark MLlib(특징, 머신러닝 분류, 데이터 유형,,Word2Vec, VectorAssembler, ChiSqSelector 등) - MLlib Algorithms(Classification, Regression, Clustering, Collaborative, Filtering, Dimensionality Reduction) - ML Pipeline(Estimator, Transformer, Paramerter, Pipeline) - Model Selection(CrossValidator, TrainValidationSplit) - ML Persistence(Status, Predictive Model Markup Language) |                               |
| Part 3. 추천시스템 구현 프로젝트                             |                               |
| 11-12                                                        | Recommender system with Spark |
| 10주간 배운 내용들을 바탕으로 Cassandra와 Redis 등을 활용하여 음악추천시스템의 기본내용을 구현해봅니다.  - 추천시스템의 개요(추천시스템 아키텍처 및 알고리즘, 배치 추천시스템과 실시간 추천시스템) - 추천시스템 구현(음악추천시스템) - 실습 데이터 : 음악 예제 데이터 |                               |