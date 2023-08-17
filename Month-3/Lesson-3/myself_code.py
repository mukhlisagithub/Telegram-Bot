# text = open('t7.txt', 'r')
# # print(text.readline())
# # print(text.readline())
# # print(text.readline())
#
# for i in text:
#     print(i)


# f = open('t7.txt', 'a')
# f.write('faylimizga yangi malumot qoshildi')
# f.close()
#
# f = open('t7.txt', 'r')
# print(f.read())
# f.close()


f = open('t7.txt', 'w')
f.write('hozir hammasi ochib ketadi')
f.close()

f = open('t7.txt', 'r')
print(f.read())

f.close()

