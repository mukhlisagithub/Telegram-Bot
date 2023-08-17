# ozidan obyekt olib bolmaydigan class => Abtract class deyiladi

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def f1(self) -> None:
        pass

    def f2(self):
        pass

class Animal2(Animal):
    def f1(self):
        print("hello")


a = Animal2()
a.f1()
# print(a.f1())