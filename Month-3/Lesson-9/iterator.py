# Iterator

class Iterator:
    def __init__(self, start=0, stop=None):
        self.indx = 0
        self.val = start
        self.ds = isinstance(self.val, str | list | tuple) # nimaligini aniqlab beradigan funksiya
        self.stop = stop
        if self.ds:
            self.stop = len(self.val)


    def __next__(self):
        if self.ds:
            temp = self.indx
            self.indx += 1
            if temp < self.stop:
                return self.val[temp]
            return None
        temp = self.val
        self.val += 1
        if self.stop:
            if temp < self.stop:
                 return temp
            return None
        return temp

a = []
# for i in range(-5,20):
#     a.append(i)
# print(a)
# a = list(range(10))
# i = iter(a)
# i = Iterator(a)
# print(i)
# for el in i:
#     print(el)
i = Iterator([1,23,3,45,67,889])
val = next(i)
while val is not None:
    print(val)
    val = next(i)




# for i in Iterator([1,2,3]):
#     print(i)
