## 메소드

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):     # 기본적인 요소 - 생성자(자동으로 호출되는 부분)
        # 멤버 변수 : 클래스 내에 정의된 변수들
        self.name = name 
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        # self : 자기자신 -> 클래스에서 메소드 앞에 항상 적어줌
        # init에서 전달받은 name을 self.name에서 사용
        self.name = name            
        self.hp = hp
        self.damage = damage


    def attack(self, location):     # 공격 방향/위치

        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]\n"    \
            .format(self.name, location, self.damage))
            # name과 damage는 self에서 정의된 변수를 사용
            # location은 attack에서 전달 받은 값을 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.\n".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염
firebat1 = AttackUnit("파이어뱃", 50, 16)   # hp = 50, damage = 16
firebat1.attack("5시")

# 공격 2번 받음
firebat1.damaged(25)
firebat1.damaged(25)


        