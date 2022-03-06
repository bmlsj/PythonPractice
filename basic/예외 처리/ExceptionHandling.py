## 예외 처리

try:
    print("나누기 전용 계산기")

    nums = []
    nums.append(int(input("첫번째 숫자 입력 : ")))
    nums.append(int(input("두번째 숫자 입력 : ")))
    nums.append(int(nums[0]/nums[1]))

    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:  # 값의 오류가 발생할 경우   ex) 숫자가 아닌 문자가 입력될 때
    print("에러! 잘못된 값을 입력했습니다.")

except ZeroDivisionError as err:
    print(err)  # 발생하는 에러를 그대로 출력해줌

except Exception as err:         # 나머지 모든 오류 
    print("알 수 없는 오류 발생")
    print(err)



finally:        # 에러와 관계없이 무조건 출력되는 부분
    print("계산기를 이용해 주셔서 감사합니다.")