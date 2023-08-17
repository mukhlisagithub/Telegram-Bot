text = 'salom 21 xayr135 ?423- '

# 2-usul:
# print(''.join(map(lambda x: x if x.isdigit() else ' ', list(text))))
# print(''.join(map(lambda x: x if x.isdigit() else ' ', list(text))).split())
# res = ''.join(map(lambda x: x if x.isdigit() else ' ', list(text))).split()
# print(*res)   # res ni oldidagi * belgisi integerga almashtirmaslik belgisi

# 1-usul:
# letters = list(text)
# for i in range(len(letters)):
#     if not letters[i].isdigit():
#         letters[i] = ' '
# letters = ''.join(letters).split()
# letters = list(map(int, letters))
# print(letters)

# 0-usul:
res = ''
for val in text:
    try:
        int(val)
        res += val
    except:
        res += ' '
res = list(map(int,res.split()))
print(res)

# Masala: Inputda ism soraladi. Ismdagi har bitta soz consolega chiqishda orqadan bittadan probel sorilishi kerak va oldindan ismdagi har bitta sozi qoshilib ketilishi kerak boladi.
# #Foydali manbalar: 2 ta yo 3 ta moduldan foydalanish kerak
#
#
# Masala-2: Foydalanuvchi bir qatorda son, soz va belgi kiritadi. Shularni ichidan sonlarni ajratish dasturini tuzing.
#
# 'salom 21 xayr135 ?423- ' => 21 135 423
#
# ''.join(map(lambda x: x if x.isdigit() else ' ', list(text)))