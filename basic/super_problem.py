## super 사용시 문제점
## 다중상속 시, 제일 먼저 상속한 부분만 호출된다.

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):

    def __init__(self):
        # super 사용시, 제일 먼저 상속 받은 Flyable 클래스만 호출된다.
        # super().__init__()

        # 다중 상속시에는 super사용하지 않고, 각각 init 사용해줌
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
