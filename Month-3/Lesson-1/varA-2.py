# Bismillahir rahmanir rahiym ...
#19.07.2023. Wednasday Python-Django-16 guruh uchun 2-oy sarlash imtihon bolgan
#21.07.2023. Friday kunidan ushbu guruh bilan 3-oy darslari boshlandi va man ham shu guruhda oqishga qaror qildm
#Imtihonda tushgan savollardan bazilarining tahlini korib chqamiz hozir:

# 1-variant 2-misol: Bir qatorda inglizcha va ozbekcha sozlar "-" orqali boglangan holda, vergullar orqali davomiy yozilgan.
#1). shu sozlardan dict yasab, kalitlarini inglizcha sozlar bilan, qiymatlarini orniga esa list korinishidagi ozbkecha
# soz va tartib raqamini joylashtirib chiqaring!
#2). 5 ta harfdan kop sozlarni (ingliz tilidagi) alohida lugatga alifbo tartibi boyicha tartiblab, dublicatlarsiz chqaring
# apple-olma, teacher-ustoz, autumn-kuz, python-pitoon, expensive-qimmat, modern-modniy, autumn-kuz, expensive-kuz, toy-o'yinchoq

# sozlar = input().split(',') # inputdagi soz birikmalarini vergul orqali ajratib olinadi
# print(sozlar)
# d = {}
# for i in range(len(sozlar)):
#     k, v = sozlar[i].split('-')
#     d[k] = [v, i + 1]
# print(d)
# i = 1
# for k in d:
#     if len(k)>5 and d[k][1] == i:
#         print(k, end=' ')
#     i+=1

## consoledagi natijaviy holat:
# apple-olma, teacher-ustoz, autumn-kuz, python-pitoon, expensive-qimmat, modern-modniy, autumn-kuz, expensive-kuz, toy-o'yinchoq
# ['apple-olma', ' teacher-ustoz', ' autumn-kuz', ' python-pitoon', ' expensive-qimmat', ' modern-modniy', ' autumn-kuz', ' expensive-kuz', " toy-o'yinchoq"]
# {'apple': ['olma', 1], ' teacher': ['ustoz', 2], ' autumn': ['kuz', 7], ' python': ['pitoon', 4], ' expensive': ['kuz', 8], ' modern': ['modniy', 6], ' toy': ["o'yinchoq", 9]}
#  teacher  python  modern

#2-usul: masalani "dictionary comprehension" usilidagi yechimi:
# sozlar = input().split(',')
# d = {(w:=sozlar[i].split('-'))[0]:[w[1],i+1] for i in range(len(sozlar))}
# print(d)
# i = 1
# for k in d:
#     if len(k)>5 and d[k][1] == i:
#         print(k, end=' ')
#     i += 1

# consoledagi natijaviy holat bir xil prosta-tak kodni ozroq minimize qldik xolos:
# apple-olma, teacher-ustoz, autumn-kuz, python-pitoon, expensive-qimmat, modern-modniy, autumn-kuz, expensive-kuz, toy-o'yinchoq
# {'apple': ['olma', 1], ' teacher': ['ustoz', 2], ' autumn': ['kuz', 7], ' python': ['pitoon', 4], ' expensive': ['kuz', 8], ' modern': ['modniy', 6], ' toy': ["o'yinchoq", 9]}
#  teacher  python  modern

#3-usul:
# sozlar = input().split(',')
# d = {(w:=sozlar[i].split('-'))[0]:[w[1],i+1] for i in range(len(sozlar))}
# print(d,' '.join([k for i, k in enumerate(d) if d[k][1] == i + 1]), sep='\n')

##Consoledagi holatning yanayam qisqargan code shakli:
# apple-olma, teacher-ustoz, autumn-kuz, python-pitoon, expensive-qimmat, modern-modniy, autumn-kuz, expensive-kuz, toy-o'yinchoq
# {'apple': ['olma', 1], ' teacher': ['ustoz', 2], ' autumn': ['kuz', 7], ' python': ['pitoon', 4], ' expensive': ['kuz', 8], ' modern': ['modniy', 6], ' toy': ["o'yinchoq", 9]}
# apple  teacher  python  modern




