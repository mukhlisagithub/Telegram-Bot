#4-masala: Farhodga funksiya tuzishga yordam bering. Funksiya 2 ta values, list va integer qabul qilsin. Listning har bir
# elementini berilgan songa kopaytirib, hosil bolgan listni qaytaruvchi funksiya tuzing.
#namuna: input: l=['PYTHOn' 'N8'] k = 3  bo'lsa:
#namuna: output: ['PYTHOnPYTHOnPYTHOn', 'N8N8N8' ] shu holatda chiqishi kerak boladi

# def f(l,a):
#     return list(map(lambda v: v*a,l))
# print(f(input().split(),int(input())))

##consoledagi natijaviy holat korinishi
# Python n8
# 3
# ['PythonPythonPython', 'n8n8n8']

#2-usul: lambda ichida lambda funksiyasi
# print((lambda l,a: list(map(lambda v: v*a, l)))(input().split(),int(input())))

# python salom
# 5
# ['pythonpythonpythonpythonpython', 'salomsalomsalomsalomsalom']

#3-usul: eng sodda usuli masalani yechishni
# def f(l,a):
#     for i in range(len(l)):
#         l[i] *= a
#     return l
# print(f(input().split(), int(input())))

# python n16
# 5
# ['pythonpythonpythonpythonpython', 'n16n16n16n16n16']

