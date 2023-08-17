#masala: Write a Python program to generate 26 text files named A,txt, B.txt and so on up to Z.txt. => Z.txtgacha A.txt, B.txt va hokazo nomli
# 26 ta matnli fayllarni hosil qiluvchi python dasturini yozing!

# for i in range(26):  # show the files
#     file_name =chr(ord('A') + i)
#     with open('t7.txt', 'w') as fayl:
#         fayl.write(chr(ord('A') + i) * (i + 1))
#
# belgilar = []  # get the symbols
# for i in range(26):
#     file_name = chr(ord('A') + i)
#     belgilar.extend(file_name)
#
# for belgi in belgilar:   # show the result
#     print(belgi)


## ustoz yechbergan usullari:
for code in range(ord('A'), ord('Z') + 1):  # range(65, 91)
    filename = chr(code) + '.txt' # => 'A.txt' to 'Z.txt' bolgan txt fayl yatartib beradi
    filename2 = filename.lower()
    with open(filename, 'w') as f:
         pass  # empty => bo'sh -> hech qanaqa ishni bajarmasdan kngi qismga o'tib ketadi
    with open(filename2, 'w') as f:
        pass






