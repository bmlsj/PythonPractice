## 표준 입출력
# 1
print("Python", "Java", sep = ", ", end = "?")     # python과 java를 ", "로 분리해줌

# 2
import sys
print("\nPython", "Java", file=sys.stdout)    # 표준 출력으로 처리
print("Python", "Java", file=sys.stderr)    # 표준 에러로 처리
print()

# 3
# 시험 성적
scores = {"수학":0, "영어" : 50, "코딩":100}

for subject, score in scores.items():       # items를 사용해 key, value를 투플 형식으로 불러옴
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(8) : 8칸 만큼의 공간에서 왼쪽 정렬
    # rjust(4) : 4칸 만큼의 공간에서 오른쪽 정렬

print()

# 4
# 은행 대기 순번표
# 001, 002, 003, ...

for num in range(1, 21):
    print("대기 번호 : "+ str(num).zfill(3))    
    # 3만큼의 공간에서 빈공간을 0으로 채워줌
print()


## 표준 입력
# 사용자 입력(input)은 항상 문자열 형태로 저장됨
answer = input("입력하세요 : ")
print("입력 값은 " + answer + " 입니다.")
print()


## 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되 총 10자리 공간을 확보하기
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시하기
print("{0: >+10}".format(500))

# 왼쪽 정렬하고, 빈칸을 _로 채우기
print("{0:_<10}".format(+500))

# 3자리 마다 콤마를 찍어주기
print("{0: ,}".format(10000000))
# 3자리 마다 콤마를 찍어주고 부호도 붙이기
print("{0:+,}".format(10000000))
# 3자리 마다 콤마를 찍어주고 부호도 붙이고, 자릿수 확보하기
print("{0:^<+30,}".format(10000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 둘째자리까지, 3번째 자리에서 반올림
print("{0:.2f}".format(5/3))
print()


### 파일 입출력
## 파일 쓰기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 40", file=score_file)
score_file.close()


## 파일 수정(뒤에 이어쓰기)
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80\n")         # 줄바꿈이 따로 없어서 표시해줌
score_file.write("코딩 : 100")       
score_file.close()


## 파일 읽기
# 한번에 모든 내용 읽어오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


# 한줄씩 읽어오기
# 몇 줄인지 알 때
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")    # 한줄 읽고, 커서는 다음 줄로 이동
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
score_file.close()


# 몇 줄인지 모를때, 끝까지 읽어오기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()


# 리스트에 넣어 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형식으로 저장
for line in lines:
    print(line, end="")

score_file.close()
