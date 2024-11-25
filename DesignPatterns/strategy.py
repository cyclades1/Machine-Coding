from abc import ABC, abstractmethod

class CarStartStrategy(ABC):
    @abstractmethod
    def start(self):
        pass

class AutoStartStrategy(CarStartStrategy):
    def start(self):
        print("auto started")


class KeyStartStrategy(CarStartStrategy):
    def start(self):
        print("key started")


class Car(ABC):

    def __init__(self):
        self.carStartStrategy = None

    def setCarStartStrategy(self, carStartStrategy:CarStartStrategy ):
        self.carStartStrategy = carStartStrategy

    def start(self):
        self.carStartStrategy.start()

    def run(self):
        print("running...")

    @abstractmethod
    def stop(self):
        pass

class PetrolCar(Car):
    def stop(self):
        print("kill petrol engine car")

class ElectricCar(Car):
    def stop(self):
        print("stop electric circuit in car")

if __name__=="__main__":
    strategy1 = AutoStartStrategy()
    strategy2 = KeyStartStrategy()

    car1 = ElectricCar()
    car1.setCarStartStrategy(strategy1)
    car1.start()
    car1.run()
    car1.stop()

    print()
    car1.setCarStartStrategy(strategy2)
    car1.start()
    car1.run()
    car1.stop()

    print()
    car1 = PetrolCar()
    car1.setCarStartStrategy(strategy1)
    car1.start()
    car1.run()
    car1.stop()

    print()
    car1.setCarStartStrategy(strategy2)
    car1.start()
    car1.run()
    car1.stop()

