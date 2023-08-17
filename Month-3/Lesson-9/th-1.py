# range => 0 dan 25 gacha list hosil qiladi

from time import perf_counter as P

# a = list(range(26))

# a = [chr(code+97) for code in range(26)]  # list comprehension
# print(a)

a = list('salom'*200000)  # salomdagi 5 ga 200000 kopaytirilyapti
start = P()
for i in range(len(a)):
    print(f"{i+1}-{a[i]}", end = ' ')

end1 = P()-start

start = P()
for i, val in enumerate(a):  # elementlarni raqamlash => "enumerate
    print(f"{i+1}-{val}", end=' ')
print(f"\nenumerate(list): {P()-start} sec")
print(f"\nrange(len(list)): {end1} sec")


# chr(97) => "a"

