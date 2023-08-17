# task-2: Laptop nomli Class e'lon qiling va unda quyidagi parameterlar va metodlar bolsin.
# Parmeterlar: firm, model, CPU, DDR, price
# Methods: laptop_info()
# laptop_info() metodi chaqirilganda barcha parameterlar haiqda malumot print qilinsin!

class Laptop:
    def __init__(self, firm, model, CPU, DDR, price):
        self.firm = firm
        self.model = model
        self.CPU = CPU
        self.DDR = DDR
        self.price = price

    def laptop_info(self):
        print(f" Laptop ishlash chiqarilgan firmaning nomi {self.firm}")
        print(f" Laptop modeli {self.model}")
        print(f" laptop's calculates devise is {self.CPU}")
        print(f" Lapptop's consume less power thing is {self.DDR}")
        print(f" Laptops price is {self.price}")


laptop = Laptop("Hewlett-Packard Company", "HP", "Calculates hard tasks", "Save less power", "$8000")
print(laptop.price)
laptop.laptop_info()