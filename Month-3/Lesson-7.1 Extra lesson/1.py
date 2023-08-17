# Revison OOP

class Car:
    # name = 'BYD'
    # year = 2023
    # electr = True
    # color = "Blue"
    def __init__(self, name, year, elc, color):
        self.name = name
        self.year = year
        self.elc = elc
        self.color = color

    def __str__(self):
        print(f'name={self.name} year={self.year}')

byd = Car("BYD", 2023, True, "Blue")
nexia = Car("Nexia", 2011, True, "White")
print(byd.name)
print(nexia.name)



# print(Car.name)
# print(Car.name)