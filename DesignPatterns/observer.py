from abc import ABC, abstractmethod
from typing import Set

class Observer(ABC):
    def __init__(self, subject:'Subject'):
        self.subject = subject
        subject.addObserver(self)
    @abstractmethod
    def notify(self, value):
        pass

class TVObserver(Observer):

    def notify(self, value):
        print("temprature on TV is {}".format(value))

class RadioObserver(Observer):

    def notify(self,value):
        print("temprature on Radio is {}".format(value))

class Subject(ABC):
    def __init__(self):
        self.observers: Set[Observer] = set()

    def addObserver(self, observer:Observer):
        self.observers.add(observer)

    def removeObserver(self, observer:Observer):
        self.observers.remove(observer)

    def notifyObserver(self, value):
        for observer in self.observers:
            observer.notify(value)

class Weather(Subject):
    def __init__(self):
        super().__init__()
        self.temp = None

    def updateTemp(self, temp):
        self.temp= temp
        self.notifyObserver(self.temp)

if __name__=="__main__":
    weather = Weather()
    radio = RadioObserver(weather)
    tv = TVObserver(weather)

    weather.updateTemp(10)
    print()
    weather.updateTemp(20)