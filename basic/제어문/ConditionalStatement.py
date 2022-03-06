## if 문

weather = input("오늘 날씨는? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")

elif weather == "미세먼지":
    print("마스크를 챙기세요")

else:
    print("준비물 필요 없어요")


temp = int(input("오늘 기온은? "))
if temp >= 30 :
    print("너무 더워요")
elif 30 > temp >= 10:
    print("괜찮은 날씨에요")
elif 10 > temp >= 0:
    print("외투를 챙기세요")
else:
    print("너무 추워요.")



### for문
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

print()


### while문
customer = "토르"
index = 5

while index > 0:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1

    if index == 0:
        print("커피가 폐기처분 되었습니다.")
    


### continue와 break
# continue : 실행시키지 않고 넘어감
# break : 반복문을 종료

absent = [2, 5]     # 결석
no_book = [7]

for stu in range(1, 11):
    if stu in absent: 
        continue
    elif stu in no_book:
        print("{0}는 교무실로 따라와".format(stu))
        break
    print("{0}, 책을 읽어봐".format(stu))
print()


### 한 줄 for문 
# 출석번호 1, 2, 3, 4 -> 앞에 10을 붙이기로 함 -> 101, 102, 103, 104
student = [1, 2, 3, 4, 4]
print(student)

student = [i+100 for i in student]
print(student)
print()


# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)
print()

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)


### 퀴즈5
# 총 택시 탑승 승객 수
# 조건1 : 승객별 운행 소요 시간 5 ~ 50분 사이 난수
# 조건2 : 소요시간 5 ~ 15분 사이의 승객만 매칭

from random import *

count = 0
for i in range(50):
    time = randint(5, 50)
    if 5 <= time <= 15:
        count += 1
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i+1, time))

    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i+1, time))


print("총 탑승 승객 : {} 분".format(count))