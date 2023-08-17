
class Laptop:
    # self. attr -> public Access modifier => class ichidan turib ham, tashqaridan ham obyekt bn ham murojaat qilsa boladi
    # self._attr -> protected
    # self.__attr -> private => tashqaridan turib murojaat qlb bomedi, class ichida muroojat qilsa boladi
    def __init__(self, model, is_gaming, price):
        self.__model = model  # attribute
        self.__gaming = is_gaming
        self._price = price

# Attribute => bitta initni ichida elon qilib, ozida faqat bir dona qiymat saqlaydigan ozgaruvchiga aytiladi
# @property => ichida qiymat saqlab turgan ozgaruvchiga yonalish berib yuboradi,ham uni qiymatini funksiyada olib berishdan tashqari, @model.seeter ozgaruvchi ham olib beradi

    @property   # getter function
    def model(self):
        return self.__model


    @model.setter  # setter function
    def model(self, val):
        self.__model = val

    @model.deleter  # bitta attribute uchun qiymatni ochirib berish
    def model(self):
        del self.__model

    @property  # decorator
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        self._price = val


if __name__ == "__main__":
    # getter => attributega murojaat qilib uni qiyamtini olish
    # setter => attributega murojaat qilib uni qiymatini ozgartirish
    acer = Laptop("Asus", True, 500)
    print(acer.model)
    acer.model = 'Acer2'
    print(acer.model)
    del acer.model   # acer modelini ocirish usuli
    # print(acer.model)
    print(acer.price)



# Class attributelarga tashqaridan murojjat qilganda getter va setter functionlar bolishi kerak