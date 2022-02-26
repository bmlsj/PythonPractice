# 딕셔너리(사전)
## key와 value로 구성


cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])       # 유재석 -> key 3의 값
print(cabinet[100])     # 김태호

print(cabinet.get(3))   # key 3의 값
print()

## get 함수와의 차이 - 없는 key의 값을 불러올 때
# print(cabinet[5])       # error 출력 후 종료 (hi 출력x)
print(cabinet.get(5))     # None 출력 후 hi까지 출력 
print("hi")

print(cabinet.get(5, "사용 가능"))      # 5의 값을 출력할 수 있음

# 값 존재 확인
print(3 in cabinet)     # 딕셔너리 안에 3의 값이 존재하는 지 확인 가능
print(5 in cabinet)

# key 새로 추가, 수정
print(cabinet)
cabinet[3] = "김종국"
cabinet[6] = "조세호"
print(cabinet)


# key 제거
del cabinet[3]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모두 삭제
cabinet.clear()
print(cabinet)