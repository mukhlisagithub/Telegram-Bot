# listdan element ochirishning ikki xil usuli bor:
# 1 => pop() -> index boyicha ochirsdi
# 2 => remove() -> birinchi uchragan elemtni ozini ochrb beradi

s = list(input())
list1 = sorted(list(set(s)))  # setni vazifasi dublictalarni ochirb tashlash
res = ''
print(s)
print(list1)
i = 1
label = ""
while s:
    data = list1 if i%2 else list1[::-1]  # i%2 -> qadam toq yoki juftligini aniqlovchi variable
    for el in data:
        c = s.count(el)
        res += el
        s.remove(el)
        if c<2:
            label += el
            # list1.remove(el)
    for x in label:
        list1.remove(x)
    label = ""
    # for el in list1[::-1]:
    #     c = s.count(el)
    #     res += el
    #     s.remove(el)
    #     if c<2:
    #         # list1.remove(el)
    #         # print(list1)
    #         label += el
    # for x in label:
    #     list1.remove(x)
    # label = ""
    # i += 1
print(res)