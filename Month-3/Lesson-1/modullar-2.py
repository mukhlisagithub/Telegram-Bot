## Modullar bilan ishlash:
# Matematik modul:
from math import lcm, gcd, log, factorial
print('EKUB(14,98) = ', gcd(14,98))
print('EKUK(14,98) = ',lcm(14,98))
print('2^x=7? x = ', log(7,2))
print('10! = ', factorial(10))
# Random moduli:
from random import randint, choice, shuffle
print('Tasodifiy son [2, 15] oraligida: ', randint(2,15))
ismlar = ['Muslimbek', 'Fazliddin', 'Alijon', 'Zufarbek']
print(f'Bugun choyxonani {choice(ismlar)} tashkilllashtiradi!')
shuffle(ismlar)  # ismlar royxatini aralashib ketadi yani tartibi ozgaradi
print('Ismlar royxati: ', ismlar)
# OS moduli: # bu modul faqat cmd yokida powershellda ishlaydi. Yoki bomasa linuxda bolsa terminalga qoyib ishlatsa ham boladi
from os import system
system('clear') #Linuxda "clear", Windowsda "cls"
print('Ekran tozalandi')
# Operator va Reduce modullari
from operator import add, sub, mul
print(add(1,2))
print(mul(4,2))
from functools import reduce
a = [2,3,5]
print(reduce(add, a))
print(reduce(sub, a))  # sub funksiyasini ishlatb bolmaydi
print(reduce(mul, a))
print(reduce(lambda i1, i2: i1+' '+i2, ismlar))  # qiyninroq func hiosblandi internetdan search qilish kerak!
# Iternools moduli
from itertools import combinations, zip_longest, permutations # => "Almashtirish"
b = [2,4,5,7,0, 10, 15]
print(list(combinations(b, 2))) # berilgan sonlardan 2 donadan olib 2talik kambinatsiya yasaladi
print(len(list(combinations(b, 2)))) # jami nechta kambinatsiya hosil bolishi un ishlatiladi
print(list(combinations(b, 3))) # jamoa tuzishda ishlatiladi
print(list(permutations(b,3))) # => dublicat oladi kambinatsiya jarayonida: telefon nomer, parollarda ishlatiladi
# print(dict(zip(ismlar, b)))
# print(dict(zip_longest(b,ismlar)))
from time import perf_counter, sleep
# Calendar moduli
from calendar import calendar, isleap
print(calendar(2100))   # nechi yil yozilsa usha yilning toliq calendarini chiqarib beradi
print("Kabisami(2024) = ", isleap(2024))
#!! yil % 4 == 0 and yil % 100 ! = 0 yoki yil % 400 == 0  => "Kabisa yili" qoidachasi
# Datetime moduli
from datetime import datetime
import datetime
print(datetime.MAXYEAR)  # 9999 eng katta mashu yilgacha hisoblab beradi
print(datetime.timezone)
# print(datetime.now())  # aynan hozirgi vohtni aniqlab beradi    mukhlisa_ciu_makhmaraimova_070403_tashkent_xadra