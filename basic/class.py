## 클래스

# 마린 : 공격 유닛, 군인, 총을 쏨
# 탱크 : 공격 유닛, 탱크. 포를 쏨(일반 모드 / 시즈 모드)
# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)

class Unit:
    def __init__(self, name, hp, damage):     # 기본적인 요소 - 생성자(자동으로 호출되는 부분)
        # 멤버 변수 : 클래스 내에 정의된 변수들
        self.name = name 
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))



# 마린과 탱크는 Unit의 인스턴스
# 객체 : class로부터 만들어지는 것들
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
# '.' 을 통해 외부에서 멤버 변수에 접근 가능하다    ex) wraith1.name
print("유닛 이름 : {0}, 공격력 : {1}\n".format(wraith1.name, wraith1.damage))


# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만듦(빼앗기)
wraith2 = Unit("레이스", 80, 5)
# 외부에서 변수 clocking을 추가 가능     
#          -> but, 추가된 변수는 그 변수를 확장한 객체만 사용 가능하다 
#             ex) wraith1에는 clocking이 없음
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

