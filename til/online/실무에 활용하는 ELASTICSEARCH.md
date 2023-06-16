**Part 1. Elasticsearch 시작하기**



1회차 Elasticsearch의 기본 개념 및 설치



#### ELASTICSEARCH 기본 개념



– Elasticsearch에 대하여
– Elasticsearch의 용어 및 개념 정리

#### ELASTICSEARCH 설치



– RPM, DEB로 설치하기
– 소스 코드로 설치하기

2회차 Elasticsearch의 기본 동작 및 플러그인



#### ELASTICSEARCH 기본 동작



– 인덱스 생성 및 삭제, 조회
– 문서 색인 및 조회
– 문서 갱신 및 삭제
– 클러스터 정보 확인하기

#### ELASTICSEARCH 플러그인



– 플러그인이란?
– 플러그인의 설치
– 한눈에 클러스터를 보기 위한 head 플러그인 활용
– 클러스터의 사용률을 보기 위한 HQ 플러그인 활용

**Part 2. Elasticsearch Basic Usage**



3~4회차 Elasticsearch의 환경 설정 및 클러스터 운영



#### ELASTICSEARCH 환경 설정



– Elasticsearch의 핵심인 elasticsearch.yml 설정
– 힙사이즈의 중요성, jvm.options
– 로그를 어떻게 모을 것인지 설정하는 log4j2.properties

#### ELASTICSEARCH 클러스터 운영



– 무중단 운영을 위한 롤링 리스타트
– 안정적인 성능 제공을 위한 샤드 분배 방법
– index setting
– 미리 정의된 template으로 인덱싱하기
– 비용을 절감하는 운영 방법 hot-warm data node

#### ELASTICSEARCH API 활용하기



– 클러스터 운영 _cluster API
– 클러스터 인덱스 마이그레이션 _reindex API
– 벌크 인덱싱 _bulk API
– 그 외 운영에 유용한 APIs

**Part 3. Elasticsearch Advanced Usage**



5~6회차 Elasticsearch 검색엔진 활용 및 성능 최적화, 모니터링



#### 검색엔진으로 ELASTICSEARCH 활용하기



– 인덱스 생성 과정
– 분석기 변경 방법
– 쿼리 생성

#### ELASTICSEARCH 색인 기능 최적화



– 필요하지 않다면 쓰지 말아야 할 기능들, _all 필드
– 미리 정해놓은 스키마로 리소스를 절약할 수 있는 static mapping 적용하기
– 인덱싱 된 데이터를 검색 결과에 반영할 수 있도록 refresh_interval 변경하기

#### ELASTICSEARCH 검색 성능 최적화



– 검색에 유리하도록 쿼리 튜닝하기
– 검색 성능을 위해 샤드 배치를 결정하는 노하우

#### ELASTICSEARCH 모니터링



– 데이터의 누락이 발생하는 순간, rejected
– _cat API로 클러스터 상태 모니터링 하기
– _stats API로 클러스터의 리소스 사용 지표 모니터링 하기

7회차 Elasticsearch의 성능 테스트 및 오픈소스 활용



#### ELASTICSEARCH 성능 테스트



– ‘어떻게 해야 정확한 성능을 테스트할 수 있을까?’ 시나리오 만들기
– 성능 테스트 환경
– 성능 테스트 결과 해석

#### 운영에 도움을 주는 오픈소스 툴



– 다양한 배치 작업이 가능한 curator
– 인덱스 데이터를 마이그레이션 할 수 있는 elasticdump
– 쉽게 배포하고, 쉽게 작업할 수 있는 ansible
– 한 순간도 놓치지 않고 모니터링 할 수 있는 외부 notification pusher 사용

**Part 4. Elasticsearch 실무자 특강**



8회차 다양한 분야에 활용되는 Elasticsearch 사례



#### 현업에서 사용 중인 ELASTICSEARCH



– e-commerce 상품 검색 플랫폼
– 로그 수집/ 분석 플랫폼
– 모니터링 플랫폼


  