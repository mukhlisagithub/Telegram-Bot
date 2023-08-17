# Polymorphism => "poly" -> kop, "morphius" - korinish
# Bitta narsaning kop korinishda uchrashi polymorpism deyiladi


# function() -> maqsad bir xil, qabul qilishi har xil
len("salom")   # maqsad bir xil yani uzunlikni chiqarish xoh string bosin, xoh int
len([1,2,3,4,4,5,6,7,])

def len(val):
    res = 0
    for i in val:
        res += 1
    return res