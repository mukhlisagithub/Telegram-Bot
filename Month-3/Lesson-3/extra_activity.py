import datetime

x = "8:18"
print(datetime.time(8,0) > datetime.time(9,0))
f = open('sam.txt', 'r')
ls = f.readlines()
print(ls)
ls2 = list()
for i in ls:
    print(i.split(','))
    ls2.append(i.split(','))
x = str(ls2[0][2]).split(':')
y = str(ls2[0][4]).split(':')
print(int(x[0]), y)
dav = input("Davlat kirgaz = ")
for i in ls2:
    if(True):
        x = str(i[2]).split(":")
        y = str(i[4]).split(':')
        if(datetime.time(int(x[0]), int(x[1])) > datetime.time(12,0) and datetime.time(int(y[0]), int(y[1])) < datetime.time(21,0) and datetime.time(int(x[0]), int(x[1])) < datetime.time(int(y[0]), int(y[1]))):
            print(i)