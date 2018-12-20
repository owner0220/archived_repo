### 실습_딕셔너리를 이용해서 점심메뉴 가게 전화번호를 보여주세요
import random

menu=['닭','삼겹살','국수','빵','비빔밥']
phonenumber={'닭':'010-111-1111','삼겹살':'010-222-2222','국수':'010-333-3333','빵':'010-444-4444','비빔밥':'010-555-5555'}
pick=random.choice(menu)

print(pick)
print(phonenumber[pick])