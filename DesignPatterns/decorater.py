from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self):
        self.name = "Pizza"

    @abstractmethod
    def getValue(self):
        pass
    @abstractmethod
    def getDesc(self):
        pass

class ThinCrust(Pizza):

    def __init__(self):
        super().__init__()
        self.name = "Thin Crust " + self.name

    def getValue(self):
        return 100

    def getDesc(self):
        print(self.name)
    

class ThickCrust(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Thick Crust " + self.name

    def getValue(self):
        return 150

    def getDesc(self):
        print(self.name)

class Topping(Pizza):

    def __init__(self, base:Pizza):
        super().__init__()
        self.base = base
        self.name = "Topping "
    
    @abstractmethod
    def getValue(self):
        pass

    def getDesc(self):
        print(self.name)

class Paneer(Topping):
    def __init__(self, base):
        super().__init__(base)
        self.price = 20
        self.name = "Paneer " + self.name + base.name

    def getDesc(self):
        print(self.name)

    def getValue(self):

        return self.base.getValue()+ self.price
    
class Tomato(Topping):
    def __init__(self, base):
        super().__init__(base)
        self.price = 10
        self.name = "Tomato " + self.name + base.name
        
    def getDesc(self):
        print(self.name)

    def getValue(self):
        return self.base.getValue()+ self.price
    
class Chicken(Topping):
    def __init__(self, base):
        super().__init__(base)
        self.price = 30
        self.name = "Chicken " + self.name + base.name

    def getDesc(self):
        print(self.name)

    def getValue(self):
        return self.base.getValue()+ self.price
    
if __name__=="__main__":
    tickpizza = ThickCrust()
    paneerThickpizza= Paneer(tickpizza)
    paneerThickpizza.getDesc()
    print("price is {}".format(paneerThickpizza.getValue()))

    print()

    tomatopaneerThickpizza = Tomato(paneerThickpizza)
    tomatopaneerThickpizza.getDesc()
    print("price is {}".format(tomatopaneerThickpizza.getValue()))

    print()
    thincrust = ThinCrust()
    chickenThickpizza= Chicken(thincrust)
    chickenThickpizza.getDesc()
    print("price is {}".format(chickenThickpizza.getValue()))