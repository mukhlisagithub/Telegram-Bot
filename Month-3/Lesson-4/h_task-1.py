# UYGA VAZIFA # OOP

# 1-task: Talaba classi e'lon qiling. Unda quyidagi property lar bolsin.
# Properties: ism, familiya, baho
# Talaba Classidan 3 ta object oling, ularning parameteriga qiymat bering. Bahosi eng eng past bo'lgan object ni ismini chiqaring.

class Talaba:
    def __init__(self, ism, familiya, baho):
        self.ism = ism
        self.familiya = familiya
        self.baho = baho

    # def tanishtir(self):
        # return f"Hello my name is {self.ism} {self.familiya}"


talaba1 = Talaba("Ali", "Valiyev", 85)
talaba2 = Talaba("Hasan", "Husanov", 75)
talaba3 = Talaba("Akrom", "Ikromov", 63)
talabalar = [talaba1, talaba2, talaba3]
for talaba in talabalar:
    if talaba.baho > 75 and 85:
        print("you pass")
    elif talaba.baho < 65:
        print('you fail')
# print(talaba1.ism)
print(talabalar)









