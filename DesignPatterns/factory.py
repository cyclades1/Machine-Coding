from abc import ABC, abstractmethod
from enum import Enum

class CarType(Enum):
    SuperCar="super"
    RacingCar = "racing"
    SimpleCar = 'simple'

class Car:
    def __init__(self, brand):
        self.brand= brand

    @abstractmethod
    def run():
        pass

class SuperCar(Car):
    def __init__(self, brand, type:CarType):
        super().__init__(brand)
        self.type = type
    def run(self):
        print("{} runs fastest !!".format(self.brand))

class RacingCar(Car):
    def __init__(self, brand, type:CarType):
        super().__init__(brand)
        self.type = type
    def run(self):
        print("{} runs fast..".format(self.brand))


class NormalCar(Car):
    def __init__(self, brand, type:CarType):
        super().__init__(brand)
        self.type = type
    def run(self):
        print("{} runs.".format(self.brand))
        
class Factory(ABC):
    @abstractmethod
    def create(self, brand):
        pass

class CarFactory(Factory):

    def create(self, brand, type:CarType):
        if type == CarType.SuperCar:
            return SuperCar(brand, type)
        elif type == CarType.RacingCar:
            return RacingCar(brand, type)
        elif type == CarType.SimpleCar:
            return NormalCar(brand, type)


if __name__=="__main__":
    carfactory =CarFactory()
    car1 = carfactory.create("ford", CarType.SimpleCar)
    car2 = carfactory.create("ferrari", CarType.RacingCar)

    car1.run()
    car2.run()

    car3 = carfactory.create("ford", CarType.SuperCar)
    car3.run()
