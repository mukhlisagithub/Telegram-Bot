# object oriented programming  => OOP
# class => object
# - properties => nouns => otlar
# - methods => verbs => fe'llar


# class Mashina:
#     def __init__(self, model, yil, rang):
#         self.model = model  # properties
#         self.yil = yil
#         self.rang = rang
#
#     def boshlash(self):   # Methods
#         print("Mashina boshlandi!")
#
#     def signal(self):
#         print("Beep!")
#
#     def tuhtatish(self):
#         print("Mashina toxtadi!")
#
#
# matiz = Mashina("matiz", 2005, "qora")
# # print(matiz.yil)
# matiz.boshlash()
# matiz.tuhtatish()
# matiz.signal()



# class Talaba:
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def get_name(self):
#         return self.ism
#
#     def get_lastname(self):
#         return self.familiya
#
#     def get_age(self, yil):
#         return yil - self.tyil
#
#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya}, tugilga yilim {self.tyil}"
#
# talaba1 = Talaba("Olim", "Olimov", 2000)
# talaba2 = Talaba("Hasan", "Husanov", 1995)
# talaba3 = Talaba("Akrom", "Alimov", 2004)
# # print(talaba1.tyil)
# print(talaba1.get_age(2023))
# print(talaba3.get_lastname())
# print(talaba2.get_name())




class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    # def get_info(self):
    #     """Talaba haqida ma'lumot"""
    #     return f"Ismim {self.ism} {self.familiya}, tugilga yilim {self.tyil}"

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil

    def set_bosqich(self, yangi_bosqich):  # biron bir xususiyatni ozgartirmoqchi bolsa, "set" metodidan foydalaniladi
        """Talabaning kursini yangilovchi method"""
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        """Talabaning bosqichini bittaga ko'paytirish """
        self.bosqich += 1

    def get_fullname(self):  # biron bir xususiyatni kormoqchi bolinsa, "get" metodidan foydalaniladi
        """Talaba haqida malumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"



talaba1 = Talaba("Olim", "Olimov", 2000)
talaba2 = Talaba("Hasan", "Husanov", 1995)
talaba3 = Talaba("Akrom", "Alimov", 2004)
# print(talaba1.tyil)
print(talaba3.get_fullname())
print(talaba3.set_bosqich(2))
print(talaba3.update_bosqich())
print(talaba3.get_fullname())




class Fan:
    """Fan nomli klass"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talaba qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        talabalar = []
        for talaba in self.talabalar:
            talabalar.append(talaba.get_fullname())
        return talabalar
        # return [talaba.get_fullname() for talaba in self.talabalar]

    def get_students_num(self):
        """Fanga yozilan talabalar soni"""
        return self.talabalar_soni

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__')]




# matematika = Fan("Oliy matematika")
# print(matematika.talabalar)
# print(matematika.talabalar_soni)
# print(talaba1)
# print(talaba1.ism)
# print(matematika.add_student(talaba1))
# print(matematika.talabalar_soni)
# print(talaba2.ism)
# print(matematika.add_student(talaba2))
# print(matematika.talabalar_soni)
# print(matematika.nomi)
# print(matematika.talabalar)
# print(matematika.talabalar[0].ism)
# print(matematika.talabalar[0].get_info())

matematika = Fan("Oliy matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba("Hasan", "Alimov", 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba2)
print(matematika.get_students())
print(see_methods(Talaba))
print(talaba1.__dict__)  # chaqirilgan funksiyaning metodlarini lugat korinishida qaytaradi
print(talaba1.__dict__.keys()) # faqat keylarini qaytarish kerak bolsa
print(see_methods(talaba1))






# class Talaba:
#     def __init__(self, ism, familiya, baho):
#         self.ism = ism
#         self.familiya = familiya
#         self.baho = baho
#
# talaba1 = Talaba("Ali", "Valiyev", 85)
# talaba2 = Talaba("Dilnoza", "Abdullaeva", 90)
# talaba3 = Talaba("Shohruh", "Rahmonov", 70)
#
# talabalar = [talaba1, talaba2, talaba3]
# min_baho = min(talabalar, key=lambda x: x.baho)
# print(min_baho.ism) # Output: Shohruh







