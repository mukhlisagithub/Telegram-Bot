#masala: Write a python pprogram to remove newline characters from a file. => fayldan yangi qator belgilarini olib tashlash dasturini tuzing!

new_line = []
with open('t7.txt', 'r') as f:
    qatorlar = f.readlines()
    for qator in qatorlar:
        qator = qator.strip()  # bo'sh joylarni olib tashlash
        if qator:  # bo'sh joylarni orniga, faqat qatorlarni qoshish
            new_line.append(qator)
    print(new_line)

# for qator in new_line:
#     print(qator)


