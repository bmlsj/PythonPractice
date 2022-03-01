## 다중 상속
# 부모가 둘 이상일 때(여러 곳에서 상속 받음)

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



# 날 수 있는 기능
class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]\n" \
            .format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
# 공격 + 날 수 있는 기능을 가져서, AttackUnit과 Flyable에게 상속 받음.  => 다중 상속

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
            AttackUnit.__init__(self, name, hp, damage)     # 공격 기능
            Flyable.__init__(self, flying_speed)            # fly 기능



# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격력x
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")      # Flyable의 fly 메소드 사용
