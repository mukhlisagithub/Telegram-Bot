# Masala: Bir qatorda sonlar beriladi, ulardan toqlarini bitta listga olib bering

# 4, 1, 5, 7,8,5,4,2,0,3,6  => [1,5,7,5,3]

# 1-usul:
# a = []
# data = input()
# for val in data.split():
#     if int(val) % 2:
#         a.append(int(val))
# print(a)
#
# # 2-usul:
# # print(list(map(int, filter(lambda x: int(x)%2, input().split()))))





m = [1,2,3,4,5,6,7,8,9]
print(m)
print(type(m))
m.append([77])
print(m)
m.pop()
print(m)