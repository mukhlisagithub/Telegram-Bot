## Fyalga malumot yozish.

# write -> File mavjud bolmasa, yangi file yaratdi
# Agar bor bolsa, eski malumotlarni ochiradi

fayl = open('natija.txt', 'w') # read, write, append
# text = "It is just file" # textni hech qanaqa muommolarsiz yozib beradi
# fayl.write(text)
words = ['book', 'hello', 'open', 'file'] # listdagi malumotlarni chiqarish 1-usuli:
# for w in words:
#     fayl.write(w+'\n')  # alohida-alohida qlb chiqarb beradi
# #2-usul:
# words = list(map(lambda v: v+'\n', words)) # kngi qatorga tushib ketadi malumotlarni hammasi har ketma ketlikdagi qatorlarda boladi
words = list(map(lambda v: v+' ', words))
fayl.writelines(words)
# fayl.write('Laptop')  # faylga qanaqa malumot yozishdan qatiy nazar hammmasini turi "string" bolishi kk

fayl.close()
