#1-masala: 'Hackathons' musobaqasida quyidagicha quiz ornatildi:
#       Istalgan string korinishidagi soz kiritiladi
#       dicti uchu key kiritiladi
#       Sozdagi harf dicti da bolsa oshani valuesini orniga oladi va sonni value ni uzunligiga qarab ozi qoyib boradi
#       Va usha qoyilgan value oldiga qoyib chiqariladi
#!!: dicti=bu "ascii" jadvaldagi kichkina harflarni key korinishda, value sini esa tartib raqamini str(value) korinishida oz ichiga oladi
##namuna: Soz kiriting: Backend => input
##namuna: 21Bcknd
#Key: ae
#!yuqoridagi key uchun dicti quyidagicha boladi: {'a': '1', 'e':'2'}

# soz = input()
# h = input()
# for i in range(len(soz)):
#     if soz[i] in h:
#         j = h.index(soz[i]) + 1
#         soz = str(j) + soz[:i] + soz[i+1:]
# print(soz)

#consoledagi natijaviy holat korinishi:
# Backend
# ae
# 21Bcknd

#2-usul: masalaning list li korinishi:
# soz = list(input())
# h = input()
# for i in range(len(soz)):
#     if soz[i] in h:
#         j = h.index(soz[i]) + 1
#         soz.remove(soz[i])
#         soz.insert(0, str(j))
# print(''.join(soz))

#natija hamon bir xil ln codega ozrow pzgartirishlar koritildi xolos
# backend
# ae
# 21bcknd


