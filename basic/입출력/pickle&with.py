## pickle
# 데이터를 파일 형식으로 저장
# 파일을 항상 바이너리 형식으로 저장 -> "wb"

import pickle

# 파일에 데이터 저장
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":40, "취미":["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file)  # profile의 정보를 profile_file에 저장
profile_file.close()


# 파일에서 데이터 읽어오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)     # 파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()



###  with  ###
# 파일 입출력을 조금 더 간편하게 가능
# 파일 close가 필요 없이 자동으로 종료해줌

## pickle 파일을 읽어오기
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


## 일반 파일에 쓰기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")


# ## 일반 파일 불러오기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())



### 퀴즈7
## 매주 1회 작성해야하는 보고서
""" - X 주차 주간보고 -
    부서 :
    이름 :
    업무 요약 :
"""
# 1주차 ~ 50주차까지의 보고서
# 조건 : 파일명은 1주차.txt, 2주차.txt, ...

for i in range(1, 51):
    with open("basic\quiz7\{0}주차.txt".format(i), "w", encoding="utf8") as report_file:
        report_file.writelines(["- {0} 주차 주간 보고 -\n".format(i), "부서 : \n", "이름 : \n", "업무 요약 : "])
