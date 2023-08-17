from sys import getsizeof

class Example:
    __slots__ = ('var1', 'var2')
    def __init__(self, v1, v2):
        self.var1 = v1
        self.var2 = v2

class Example2:
    def __init__(self, v1, v2, v3):
        self.var1 = v1
        self.var2 = v2
        self.var3 = v3


obj = Example(1,2)
# obj.var3 = 10 # -> tashqaridan qiymat berolmaymiz error oladi slotni ichidagina elon qilsak ishlaydi, aks holda yoq
obj2 = Example2(3,4,[1,2,['string', 'hi']])
obj2.var3 = 10
obj2.var3 = 14
# print(obj.__dict__)  # error beradi yoki dictionary ishlaydi yoki  slot ishlaydi bir vaqtning ozida

print(getsizeof(obj))
print(getsizeof(obj2))
print(getsizeof([1,2,['hello', 'hi']]))
print(getsizeof(Example))
print(getsizeof(Example2))



# a  [] # list dynamic => xotiradan xohlagancha joy egallaydi
# int a[5]; [][][][][]  => # static xotiradan faqat ajratilgan joyga ishlatolidi



# xotiradan kam joy egallashi va tashqaridan ham nuqta qlb chaqirishni oldininolish uchun abstract classdan foydalaniladi