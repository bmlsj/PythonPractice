### 리스트 []

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?  # 위치 찾기
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 탈 때        # 리스트 추가
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 - 조세호 사이에 태워봄
subway.insert(1, "정형돈")      # 1번 위치에 '정형돈' 추가됨
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())         # 맨 뒤 요소 제거
print(subway)

print(subway.pop())         # 맨 뒤 요소 제거
print(subway)


# 같은 이름의 사람이 몇 명 있는 지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
print()

# 리스트 정렬
num_list = [5, 4, 2, 1, 3]
print(num_list)
num_list.sort()
print(num_list)

# 순서 뒤집기 
num_list.reverse()
print(num_list)

# 리스트 요소 모두 지우기
num_list.clear()
print(num_list)


# 리스트 안에 다양한 자료형을 넣을 수 있음
mix_list = ["유재석", 100, True]
print(mix_list)

# 리스트 확장 : 두 리스트 합치기
num_list.extend(mix_list)
print(num_list)