# Kod quyidagicha yozilishi mumkin:
#
# python

class Laptop:
    def __init__(self):
        self._model = ""
        self._rang = ""

    def getModel(self):
        return self._model

    def setModel(self, model):
        self._model = model

    def getRang(self):
        return self._rang

    def setRang(self, rang):
        self._rang = rang


class HP(Laptop):
    def getInfo(self):
        return f"{self.getModel()} {self.getRang()}"


obj1 = HP()
obj1.setModel(input("Modelni kiriting: "))
obj1.setRang(input("Rangni kiriting: "))

obj2 = HP()
obj2.setModel(input("Modelni kiriting: "))
obj2.setRang(input("Rangni kiriting: "))

print(obj1.getInfo())
print(obj2.getInfo())

# Qiymatlarni o'zgartirish
obj1.setModel("Pavilion Black")
obj2.setRang("Gold")

print(obj1.getInfo())
print(obj2.getInfo())




# Bu kod yordamida Laptop nomli bir class yaratamiz, unda model va rang nomli protected turdagi propertylar mavjud. Getter va setter funksiyalarni tuzish uchun getModel, setModel, getRang va setRang metodlarini qo'shamiz.
#
# Keyin HP nomli voris class ni yaratamiz, bu class Laptop classidan voris oladi. getInfo metodi orqali qiymatlarni olishimiz mumkin.
#
# Dasturda 2 ta HP obyektini yaratamiz va foydalanuvchidan model va rangni kiritishni so'raymiz. getInfo metodi orqali obyektning ma'lumotlarini chop etamiz.
#
# Keyin setModel va setRang metodlar orqali qiymatlarni o'zgartirib, yana getInfo metodi orqali yangi ma'lumotlarni chop etamiz.