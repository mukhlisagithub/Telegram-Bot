# Kod
# quyidagicha
# yozilishi
# mumkin:
#
# python

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def getModel(self):
        pass


    @abstractmethod
    def getPrice(self):
        pass



class Sedan(Car):
    def getModel(self):
        return "Sedan"


    def getPrice(self):
        return 25000


class SUV(Car):
    def getModel(self):
        return "SUV"

    def getPrice(self):
        return 35000


class Hatchback(Car):
    def getModel(self):
        return "Hatchback"

    def getPrice(self):
        return 20000



obj1 = Sedan()
obj2 = SUV()
obj3 = Hatchback()

print(obj1.getModel())
print(obj1.getPrice())

print(obj2.getModel())
print(obj2.getPrice())

print(obj3.getModel())
print(obj3.getPrice())




# Bu
# kod
# yordamida
# Car
# nomli
# bir
# abstract


# class yaratamiz.Bu classda getModel va getPrice nomli abstract metodlar mavjud.Abstract metodlar tanlanmayan funksiyalardir va voris classlarda qayta yozilishi shartdir.
#
#
# Keyin
# Sedan, SUV
# va
# Hatchback
# nomli
# voris
# classlarni
# yaratamiz, Car
# classidan
# voris
# oladi
# va
# abstract
# metodlarni
# qayta
# yozadi.
#
# Dasturda
# 3
# ta
# obyekt
# yaratamiz, har
# biri
# uchun
# qiymatlar
# kiritamiz
# va
# getModel
# va
# getPrice
# metodlarini
# chaqiramiz.Bunda
# Sedan, SUV
# va
# Hatchback
# obyektlari
# uchun
# belgilangan
# qiymatlar
# chop
# etiladi.