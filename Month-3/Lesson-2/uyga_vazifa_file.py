# T masalalari:
#T1: Ixtiyoriy faylning oxirgi qatorini ekranga chiqaring.
# fayl = open('file.txt', 'w')
# fayl.write('book')
# fayl.close()

# fayl = open('file.txt', 'r')
# # test = fayl.read().split()
# test = fayl.readlines()[21]
# print(test)
# fayl.close()


#T2: Ixtiyoriy fayl nechi qatordan iborat ekanligini aniqlovchi dastur tuzing.
# fayl = open('file.txt', 'r')
# # test = fayl.read().split()
# test = fayl.readlines()
# print(f'Faylda {len(test)} qator bor ekan')
# fayl.close()



#T3: Ixtiyoriy fayl ichidagi eng uzun sozni aniqlovchi dastur tuzing.
# fayl = open('file.txt', 'r')
# test = fayl.readlines()
# print(len(''.join(test).replace('\n', ' ')))
# print(len(test))
# fayl.close()



#T4: Bitta fayldagi malumotni ikkinchi faylga kochiruvchi dastur tuzing.




#T6: Ushbu fayldagi T harfi bilan boshlanmaydigan qatorlar sonini aniqlovchi function tuzing.
# def count_lines(file):
#     count = 0
#     with open(file, 'r') as f:
#         for line in f:
#             if not line.startswith('T'):
#                 count += 1
#     return count
#
# file = "t7.txt"
# line_count = count_lines(file)
# print("Number of lines not starting with 'T':", line_count)


# ## ustoz yechib bergan usullari:
# def lineCount(filename, char):
#     with open(filename, 'r') as f:
#         qatorlar = f.readlines()
# # print(list(map(lambda q: q[0] != "T", qatorlar)))  # condition berilganda "true" and "false" qiymat qaytarib beradi
#     return sum(map(lambda q: q[0] != char, qatorlar))  # sum => funksiyasi nechtaligini chiqarb beradi
#
# if __name__ == "__main__":  # faylni nomi "main" bolgandagin aishga tushadi , aks holda ishlamedi
#     faylnomi = 't7.txt'
#     char = "T"
#     print(lineCount(faylnomi, char))



#T7: Ushbu faylda jami nechta soz borligini aniqlovchi dastur tuzing.
# f = open('t7.txt', 'r')
# p = f.readlines()
# print(len(''.join(p).replace('\n', ' ').split()))



#T8: Ushbu faylda "is" sozi nechinchi marotaba ishlatilganligini aniqlovchi function tuzing.
# def word_count(file):
#     count = 0
#     f = open(file, 'r')
#     for line in f:
#         words = line.split()
#         for word in words:
#             if word.lower() == 'is':
#                 count += 1
#     f.close()
#     return count
#
# result = word_count(file)
# print("Number of times 'is' is used:", result)


## ustoz yechberganlari:
# def numberOfIs(filename, word): # funksiya nomi doimo kichik harf boshlnadi, ln soz bir nechta birikmalardan tashkil topgan bolsa, birinchi harf kishik qolganlarining bosh hari katta harf bilan yoziladi
#     with open(filename, 'r') as currentfile:
#             words = currentfile.read().split() # butun boshli matni bitta string qberadi kak bitta qoshtirnooqa olib beradi. split => sozma -soz ajratib beradi
#     return len(list(filter(lambda val: val.lower() == word, words)))
#     # res =0
#     # for soz in sozlar:
#     #     res += soz.lower() == 'is'
#     # print(res)
#     # print(sozlar)
#     # print(list(filter(lambda soz: soz.lower() == 'is', sozlar)))
#
# if __name__ == "__main__":
#     print(numberOfIs('t7.txt', 'is'))




# words = currentfile.read().split()   => collecting all words of the file as list => comments are very useful for interview


#T9: Ushbu faylda 5ta harfdan kichkina bolgan sozlarni nechta ekanligini aniqlovchi function tuzing.
# l = open('t7.txt', 'r')
# m = l.readlines()
# # print(len(m))
# i = 1
# for k in m:
#     if len(m)<5:
#         print(m)
#     i += 1



#T10: Ushbu faylda katta harflar bilan boshlanadigan sozlarni boshqa faylga kochiring.
def movingWords(inputfile, outputfile):
    # currentfile = open(inputfile, 'r')
    # word = currentfile.read().split()
    # currentfile.close()

    with open(inputfile, 'r') as currentfile:
        words = currentfile.read().split()    # collecting all words of the file as list
    with open(outputfile, 'w') as currentfile:
        currentfile.write('\n'.join(list(filter(lambda val: val[0].isupper(), words))))

if __name__ == "__main__":
    movingWords('t7.txt', 'result.txt')
