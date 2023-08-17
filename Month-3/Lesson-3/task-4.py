#masala: Write a python program to extract characters from various text file and puts them into a list. => Turli matnli fayllardan belgilar
# ajratib olish va ularni ro'yxatga kiritish uchun python dasturini dasturini yozing.

symbols = []
with open('t7.txt', 'r') as f:
    qatorlar = f.readlines()
    for qator in qatorlar:
        qator = qator.strip()
        for symbol in qator:
            if symbol not in symbols:
                symbols.append(symbol)
    print(symbols)


# for symbol in symbols:
#     print(symbol)
