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
print()


## 퀴즈 8
# 총 3대의 매물이 존재합니다.
# 강남, 아파트, 매매, 10억, 2010년
# 마포, 오피스텔, 전세, 5억, 2007년
# 송파, 빌라, 월세, 500/50, 2000년

class House:

    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

        # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f"총 {len(houses)}대의 매물이 존재합니다.")
for house in houses:
    house.show_detail()
    