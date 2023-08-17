# Bu
# vazifani
# bajarish
# uchun
# Python
# dasturlash
# tilidan
# foydalanamiz.Quyidagi
# kodni
# ishga
# tushirish
# orqali
# input.txt
# faylidan
# ma
# 'lumotlarni o'
# qiyapmiz
# va
# natijalarni
# ekranga
# chiqaramiz:
#
# python
# Faylni ochish

with open("input.txt", "r") as file:
    # Fayldan qatorlar ro'yxatini olamiz
    lines = file.readlines()

    # Qatorlar sonini chiqaramiz
    num_lines = len(lines)
    print("Qator =", num_lines, "ta")

    # Har bir qatorda nechtadan so'z borligini topamiz va chiqaramiz
    word_counts = []
    for line in lines:
        words = line.split()
        word_count = len(words)
        word_counts.append(word_count)

    print("Sozlar =", word_counts)

# Kodni
# yuklab
# olish
# va
# input.txt
# faylini
# birinchi
# qatorida
# joylashgan
# skript
# fayliga
# saqlab
# qo
# 'ying. Skriptni ishga tushirish uchun terminalda quyidagi komandani yozing:
#
# python
# script.py
#
# Natijada, stdout - da
# quyidagi
# chiqadi:
#
# Qator = 3
# ta
Sozlar = [2, 4, 4]