# task-3: Calculator classini tuzing. U quyidagi parameter va metodlarga ega bolsin.
# Parameters: num1, nums
# Methods: sum(), mul(), div(), sub()
# Tuzilgan class asosida abyekt yasang. Methodlar chaqirilgan payt, ekranga classdagi ikki son ortasida
# amallar bajarilish natijasi chop etilsin.


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def sum(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def sub(self):
        return self.num1 - self.num2

calc = Calculator(2,3)
print(calc.sum())
print(calc.mul())
print(calc.div())
print(calc.sub())


