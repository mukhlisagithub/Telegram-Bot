fayl = open('natija.txt', 'r')
# data = fayl.read().split() # har bitta sozni probel orqali ajratdi
data = fayl.readlines() #readlines => har bitta qatorni listni bir elemnetni kornishi sifatida qaytaradi
#readlines orqali indexga murojaat qlsa ham boladi
print(f'Faylda {len(data)} qator bor ekan')  # len funksiyasi orqali textda nechta qator borligini aniqlab beradi
print(data[len(data) // 2])  # textdagi qatorning ortasini topish usuli
# print(data)
print(len(''.join(data).replace('\n', ' ').split()))  # textda nechta soz borligi aniqlab ebradi
fayl.close()