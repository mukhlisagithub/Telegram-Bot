## 'natija.txt' fayldan malumotni oqib olish:
## "READ" => umumiy hammma qatorni oqib oladi
## "READLINE" => faqat bitta qatorni oqib oladi

# # sozlar = input() # input funksiya berilgan matni bir qatorda oqib oladi
# fayl = open('natija.txt', 'r') # read
# sozlar = fayl.read().split()  # splitga olsa ham boladi oqib olishda faqat
# print(sozlar)
# fayl.close()


#task: bir qatorda berilgan sonlar yigindisi ikkinchi qatordagi sondan kattami, kichikmi?
fayl = open('natija.txt', 'r') # read
a,b = map(int, fayl.readline().split())   # readline -> faqat bir dona qatorni oqib olish uchun
c = int(fayl.readline())
print(a+b > c)
fayl.close()