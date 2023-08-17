from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def getModel(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass


class DellLaptop(Laptop):
    def __init__(self, model, price):
        self._model = model
        self._price = price

    def getModel(self):
        return self._model

    def getPrice(self):
        return self._price


class HP_Laptop(Laptop):
    def __init__(self, model, price):
        self._model = model
        self._price = price

    def getModel(self):
        return self._model

    def getPrice(self):
        return self._price


class LenovoLaptop(Laptop):
    def __init__(self, model, price):
        self._model = model
        self._price = price

    def getModel(self):
        return self._model

    def getPrice(self):
        return self._price


obj1 = DellLaptop("Dell XPS 13", 1500)
obj2 = HP_Laptop("HP Spectre x360", 1200)
obj3 = LenovoLaptop("Lenovo ThinkPad X1 Carbon", 2000)

print(obj1.getModel(), obj1.getPrice())
print(obj2.getModel(), obj2.getPrice())
print(obj3.getModel(), obj3.getPrice())


# stdout:
#
# Dell XPS 13 1500
# HP Spectre x360 1200
# Lenovo ThinkPad X1 Carbon 2000