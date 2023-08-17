# a => append => bor malumot davomidan malumot yozish
# Agar fayl bolmasa, Error beradi, fayl bolishi majburiy

with open('natija.txt', 'r') as f:
# fayl.write('The End2. \n')  # oxiriga malumot qoshish
    data = f.readlines()

data.insert(0, 'Start: \n')

with open("natija.txt", 'w') as f:
    f.writelines(data)

# with kalit sozi ishlatilganda "close" funksiyasini ishlatmasa ham boladi, uni avtamatichiski uzi close qiladi

