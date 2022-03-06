## 투플 () ##
# 리스트보다 속도가 빠름
# 변경되지 않는 목록을 사용할 때   -> add 함수가 사용 불가해, 값 추가 불가능

menu = ("돈까스", "치즈까스")   # 메뉴를 변경하지 않음
print(menu[0])
print(menu[1])

# 투플을 이용해 많은 값을 한번에 넣을 수 있음
name, age, hobby = "김종국", 40, "코딩"
print(name, age, hobby)
print()



## 집합 (set) {} ##
# 중복이 안됨. 순서가 없다.
my_set = {1, 2, 3, 3, 3}        # {1, 2, 3}이 출력됨
print(my_set)


java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])      # 리스트를 set으로 표현 가능


# 교집합 출력 (python과 java가 모두 가능한 사람)
print(java & python)
print(java.intersection(python))
print()

# 합집합 (java나 python 둘 중 하나라도 가능한 사람)
# 순서가 없어 무작위로 출력됨
print(java | python)
print(java.union(python))
print()

# 차집합 (java - python : java는 할 수 있지만 python은 불가능한 사람)
print(java - python)
print(java.difference(python))
print()

# 값을 추가 - python을 할 수 있는 사람이 증가
print(python)
python.add("김태호")
print(python)
print()

# 값을 제거 - java를 잊어버림
print(java)
java.remove("김태호")
print(java)
print()


### 자료 구조의 변경 ###
menu = {"커피", "우유", "주스"} # set
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))
print()



### 퀴즈4
## 댓글 이벤트를 진행 -> 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰
## 조건1 : 댓글을 20명이 작성하였고, 아이디는 1~20
## 조건2 : 댓글 내용과 상관없이 무작위로 추첨 but 중복 불가
## 조건3 : random의 shuffle과 sample 활용

from random import shuffle, sample
user = list(range(1, 21))
shuffle(user)

winning =sample(user, 4)

chicken = winning[0]
coffee = winning[1:]
print(f"치킨 당첨자 : {chicken}, 커피 당첨자 : {coffee}")