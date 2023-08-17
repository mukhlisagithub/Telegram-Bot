# Bismillahir rahmanir rahiym..

# OOP => OBJECT ORIENTED PROGRAMMING

# Python Basic => Conditionals, Loops, data types, data struct, funstions, file IO, exceptions

# a = [45]
# a.append(50)
#
# def findElement(a: list, el: int):
#     pass


class Car:
    # __functionName__  => Dunder Methods => Double Underscore MEthods
    def __init__(self, val1, val2 ):  # konstructor - initialize => boshlangich qiymat berish
        self.color = val1
        self.model = val2

    def signal(self, count):
        print(f'{self.model}:{"Beep "  *count}')

    def __str__(self):
        return f'This is a {self.model}!'

c1,m1 = input('Color:'), input('Model: ')
obj = Car(val2=m1, val1=c1)
print(obj.color, obj.model)
obj.signal(2)
print(obj)

# obj1 = Car('rang1', 'model1')
# obj2 = Car(val2 = 'model2', val1 = 'rang2')
# obj1.color = 'Black'
# obj2.color = 'White'
# obj1.model = 'BMW'
# print(type(obj1))
# print(obj1.color, obj1.model)
# print(obj2.color, obj2.model)
# a = 45
# print(type(a))

