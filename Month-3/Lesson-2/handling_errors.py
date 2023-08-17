# a, b = input() # ValueError
# print('1' + 2)  # TypeError => turdagi xatolik : stringga integer qoshib bomaydi
# print([1,2,3][5])  # IndexError => mavjud bolmagan indexni sorash
# open('input.txt', 'r') # FileNotFoundError => read mode da file bolishi shart, bolmasa shunaqa error beradi
# print(a) # NameError => mavjud bolmagan nomni chaqrish
#     print() # IndentationError => probel xatoligi

# xatolikni oldini oladigan "try" and "except" sozlari:
# try:
#     # print('a' + 1)
#     # # print('a' [1])
#     print(4/2)
# finally:
#     pass
# except TypeError:
#     print('Error type')
# except IndexError:
#     print('Index is not found')
# except:
#     print("Other Error")
# else:                               #=> xatoli bolmagandagina ishlaydigan qism "else"
#     print("Success")
# finally: # finallyni olib tashlasa ham printddgi malumot ishlaydi
#     print('Bu har doim ishlaydi') # har doim ishlaydigan kalit soz "finally"


#task:
try:
    age = int(input('Yoshingiz nechida: '))
    if age < 1:
        raise ValueError  # biro
except:
    print('Bunaqa yosh yoq')
else:
    print(f'siz {age} yoshdasiz')

