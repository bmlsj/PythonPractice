# 연산자 구하기

print(1+1)
print(2**3)     # 2^3
print(5%3)      # 나머지 구하기
print(10%3) 

print(10//3)    # 몫 구하기
print()

# 숫자 함수
print(abs(-5))      # 5
print(pow(4, 2))    # 4^2 = 16
print(max(5, 12))   # 12
print(min(5, 12))   # 5
print(round(3.14))  # 3 -> 반올림
print(round(4.99))  # 5

from math import * 
print(floor(4.99))  # 내림 4 
print(ceil(3.14))   # 올림 4
print(sqrt(16))     # 제곱근 4.0
print()


# 랜덤 함수
from random import *

print(random())     # 0.0 ~ 1.0 미만의 임의의 값
print(random()*10)  # 0.0 ~ 10.0 미만의 임의의 값

print(int(random()*10)) # 0 ~ 10 미만의 임의의 값
print(int(random()*10 + 1)) # 1 ~ 10 이하의 임의의 값
print(int(random()*45 + 1)) # 1 ~ 45 이하의 임의의 값

print(randrange(1, 45))     # 1 ~ 45 미만의 임의의 값
print(randint(1, 45))       # 1 ~ 45 이하의 임의의 값
print()


# quiz
# 월 4회 스터디 -> 1번은 오프라인, 3번 온라인
# 1 ~ 3일은 제외, 28일 이내

studyDay = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 %d 일로 선정되었습니다."%(studyDay))