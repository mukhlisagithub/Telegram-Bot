from random import random

# Faylni ochish va harflarni o'qish
with open("harflar.txt", "r") as file:
    letters = file.read()

# Foydalanuvchidan so'zlarni olish
words = input("So'zlarni vergul orqali kiritin: ").split(",")

# Harflardan foydalanib so'zlarni yasash va qaysilar ekanligini chiqarish funktsiyasi
def count_occurrences(letters, words):
    occurrences = []
    for word in words:
        count = 0
        for letter in letters:
            if letter.lower() == word.lower():
                count += 1
        occurrences.append(count)
    return occurrences

# Natijalarni chiqarish
result = count_occurrences(letters, words)
for i in range(len(words)):
    print(f"{words[i]} so'zi {result[i]} marta yasab bo'lishi mumkin")


# Bu skriptni ishga tushirish uchun terminalda quyidagi komandani yozing:
#
#
# python script.py
#
#
# Faylni o'qish va foydalanuvchidan so'zlarni kiritishdan so'ng, stdout-da natijalar chiqadi:
#
#
# So'zlarni vergul orqali kiritin: book,Win,Python
# book so'zi 1 marta yasab bo'lishi mumkin
# Win so'zi 3 marta yasab bo'lishi mumkin
# Python so'zi 0 marta yasab bo'lishi mumkin