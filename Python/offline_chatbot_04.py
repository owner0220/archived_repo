### 실습_숫자 45개 중 로또 숫자 5개를 뽑아보자
import random

lotto=range(1,46)  #range는 range(1,46) **오른쪽 숫자보다 1 작은 수까지 수열 결과 보여준다.**
lotlist=random.sample(lotto,5)

print(lotlist)