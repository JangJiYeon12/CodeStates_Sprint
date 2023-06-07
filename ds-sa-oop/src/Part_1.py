class CarOwner:
    """
    자동차 주인을 나타내는 클래스입니다. 
    자동차 주인은 이름(name)을 가지고 있으며
    자동차 주인은 concentrate 메소드를 통해 이름 + ' can not do anything else'를 반환해야합니다. 
    """
    def __init__(self, name):
        self.name = name

    def concentrate(self):
        return f'{self.name} can not do anythong else'


class Car:
    """
    자동차를 나타내는 클래스입니다. 
    자동차는 주인(owner)을 가지고 있으며, 주인은 CarOwner를 통해서 생성됩니다.
    자동차는 drive 메소드를 통해 
    자동차 주인이 집중하고 있으며(concentrate), 누가 운전하고 있는지 반환해야합니다. 
    '{자동차주인이름} is driving now.'
    """
    def __init__(self, owner_name):
        self.owner = CarOwner(owner_name)

    def drive(self):
        return f"{self.owner.concentrate()}\n{self.owner.name}  is driving now."


class SelfDrivingCar(Car):
    def drive(self):
        """
            drive 메소드를 통해
            'Car is driving by itself'를 반환해야합니다. 
            메소드 오버라이딩 개념을 다시 생각해보며 코드를 작성해주세요.
        """
        return 'Car is driving by itself'

