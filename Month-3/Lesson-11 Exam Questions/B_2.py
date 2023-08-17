# python

sozlardagi_harflar = (2, 1, 4, 5)

qator_gap = input("1 qator gapni kiriting: ")

undosh_belgilar = ""
unli_belgilar = ""

for harf in qator_gap:
    if harf.isalpha():
        if sozlardagi_harflar.count(1) > 0:
            undosh_belgilar += "*"
            sozlardagi_harflar = tuple(filter(lambda x: x != 1, sozlardagi_harflar))
        else:
            unli_belgilar += "*"
            sozlardagi_harflar = tuple(filter(lambda x: x != 2, sozlardagi_harflar))
    else:
        undosh_belgilar += harf
        unli_belgilar += harf

with open("undosh.txt", "w") as f:
    f.write(undosh_belgilar)

with open("unli.txt", "w") as f:
    f.write(unli_belgilar)



# Bu kod foydalanuvchidan 1-qator gapni olib, undosh.txt va unli.txt fayllariga
# mos ma'lumotlarni yozadi. Har bir harfni tekshirib, agar undosh harf bo'lsa undosh_belgilar o'zgaruvchisiga "*" qo'shadi,
# agar unli harf bo'lsa unli_belgilar o'zgaruvchisiga "*" qo'shadi. Agar harf raqam yoki belgi bo'lsa, undosh_belgilar va unli_belgilar o'zgaruvchilariga o'z harflarini qo'shadi.