## 슬라이싱
# 필요한 정보만 추출해서 사용

jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연도 : " + jumin[:2])    # 0부터 1번째까지
print("월 : " + jumin[2:4])     # 2~3번째자리
print("일 : " + jumin[4:7])

print("생년월일 : " + jumin[:6])    # 처음부터 6직전(5)까지
print("뒤 7자리 : " + jumin[7:])    # 7번째부터 끝까지
print("뒤 7자리(뒤에서 계산) : " + jumin[-7:])  # 뒤에서 7번째부터 끝까지, 맨끝이 -1
print()


## 문자열 처리 함수
python = "Python is Amazing"

print(python.lower())           # 모두 소문자로
print(python.upper())           # 모두 대문자로
print(python[0].isupper())      # 0번째 문자가 대문자인지 : True
print(len(python))              # 문자열 길이
print(python.replace("Python", "Java"))     # 'Python'문자를 'Java'로 교체


# index 함수
index = python.index("n")       # n의 인덱스 위치를 알려줌
print(index)

index = python.index("n", index + 1)    # (index + 1)의 위치부터 n을 찾음 -> (찾을 문자, 시작 위치)
print(index)


# find 함수
print(python.find("n"))


# find와 index 의 차이
print(python.find("Java"))      # 원하는 값이 없을 때, -1 출력
# print(python.index("Java"))     # 원하는 값이 없을 때, error 출력후 종료

# count 함수
print(python.count("n"))        # n의 갯수
print()



## 문자열 포맷 방식

print("a"+"b")
print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s살 입니다." % 20)
print('나는 %s를 좋아해요.' % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))
print()

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))

# 방법 4
age= 20
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")   # 실제 변수값을 출력 가능 
print()

## 탈출 문자
# \n : 줄바꿈
# \', \" : 문장 내에서 ', " 출력
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \ 출력
print("C:\\User")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")    # PineApple 이 출력됨

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")        # RedApple 출력

# \t : tab역할
print("Red\tApple")
print()


### 퀴즈
# 사이트 별로 비밀번호를 만들어 주는 프로그램
url = "http://naver.com"
rule12 = url[7:12]
rule3 = rule12[:3] + str(len(rule12)) + str(rule12.count("e")) + "!"
print(f"{url}의 비밀번호는 {rule3}입니다.")

my_str = url.replace("http://", "")     # rule1
my_str = my_str[:my_str.index(".")]     # rule2 : .전까지
pwd = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(pwd)

