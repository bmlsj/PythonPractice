## 함수
## 1
from unicodedata import name
from pip import main


def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):        # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance+money

def withdraw(balance, money):      # 출금
    if balance >= money : 
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money):     # 저녁에 출금
    commission = 100    # 야간 수수료
    return commission, balance - money - commission     # 수수료와  현재 잔액을 투플 형식으로 보여줌

balance = 0     # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 200)
commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission}원이며, 잔액은 {balance}원입니다.")



## 2 - 기본값
def profile(name, age, main_lang):
    print("이름은 :{0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석", 30, "파이썬")
profile("김태호", 23, "자바")
print()

# 같은 학교, 같은 학년, 같은 반, 같은 수업일 경우 -> 불필요하게 매번 적어줄 필요가 없음
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름은 :{0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")
print()


## 3 - 키워드 값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")
print()


## 4 - 가변인자
# end = " "를 사용해, 문장뒤에 연결해줌
def profile(name, age, *language ):
    print("이름은 :{0}\t나이 : {1}".format(name, age), end=" ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("유재석", 30, "파이썬", "java", "c", "c++", "c#")
profile("김태호", 23, "자바", "kotlin", "swift")
print()


## 5 - 지역 변수(함수 내)와 전역 변수(프로그램 전체)

gun = 10
def checkpoint(soldiers):   # 경계근무
    global gun              ### 전역 공간에 있는 변수 gun을 사용할 수 있다.
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


# 전역 변수 많이 사용 -> 코드 관리 하기 어려움(권장x)
# 되도록 파라미터값으로 사용 후 반환
def checkpoint_ret(gun, soldiers):
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2)               # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
print()


### 퀴즈 6
## 표준 체중을 구하는 프로그램
## 남자 : 키(m) x 키 x 22
## 여자 : 키(m) x 키 x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산하기
#       * 함수명 : std_weight
#       * 전달값 : 키(height), 성별(gender)

# 조건2 : 표준 체중은 소수점 둘째자리까지 표시  -> round 함수를 사용


def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    
    else:
        return height * height * 21

height, gender = 1.75, "남자"
weight = std_weight(height, gender)
print("키 {0}cm {2}의 표준 체중은 {1}kg입니다.".format(int(height*100), round(weight, 2), gender))