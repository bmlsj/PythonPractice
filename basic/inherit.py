## 상속


# 일반 유닛
class Unit:
    def __init__(self, name, hp):    
        self.name = name 
        self.hp = hp
        print("{0} 유닛이 생성되었습니다.".format(self.name))



# 공격 유닛 = 일반 유닛(이름, 체력) + 공격력
# Unit 클래스를 상속 받아 작성됨
class AttackUnit(Unit):   
    def __init__(self, name, hp, damage):
        # Unit의 name, hp를 상속
        Unit.__init__(self, name, hp)  
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


# 메딧 : 의무병, 공격력x.
