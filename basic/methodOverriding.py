## 메소드 오버라이딩
# 자식 클래스에서 정의한 메소드를 사용하고 싶을때, 메소드를 새롭게 정의해서 사용


# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):    
        self.name = name 
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(self.name))


    def move(self, location):       # 유닛의 이동
        print("\n[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"   \
                .format(self.name, location, self.speed))



# 공격 유닛 = 일반 유닛(이름, 체력) + 공격력
# Unit 클래스를 상속 받아 작성됨
class AttackUnit(Unit):   
    def __init__(self, name, hp, speed, damage):
        # Unit의 name, hp를 상속
        Unit.__init__(self, name, hp, speed)  
        self.damage = damage


    def attack(self, location):     # 공격 방향/위치
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]\n"    \
            .format(self.name, location, self.damage))


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

    def fly(self, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]\n" \
            .format(self.name, location, self.flying_speed))


# 공중 공격 유닛 클래스
# 공격 + 날 수 있는 기능을 가져서, AttackUnit과 Flyable에게 상속 받음.
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
            # 지상 유닛의 speed가 필요 없음 -> 0으로
            AttackUnit.__init__(self, name, hp, 0, damage)     # 공격 기능
            Flyable.__init__(self, flying_speed)            # fly 기능

    # 일반 유닛의 move를 새롭게 재정의
    def move(self, location):
        print("\n[공중 유닛 이동]")
        self.fly(location)



# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀 크루저 : 공중 유닛, 체력도 좋, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

