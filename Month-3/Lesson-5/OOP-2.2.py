# Masala: Calc nomli class yarating. add function bolsin

# class Calc:
#     def add(self, val1, val2):
#         return val1 + val2
#
#
# if __name__ == "__main__":
#     obj = Calc()
#     print(obj.add(2,5))




class ExampleClass:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "Bu class ning nomi ExampleClass"

    def __str__(self):  # yuz foiz stringga aylantirgan payt ishladyi
        return "This is ExmpleClass"

    def __bool__(self):  # True false qaytaruvchi class
        # return 2>1
        # return bool(self.name)
        try:
            return bool(self.name)
        except:
            return False

    def __add__(self, other):
        new_obj = ExampleClass(self.val)
        if isinstance(other, ExampleClass):
            if isinstance(new_obj.val, int | float):
                 new_obj.val += other.val
            else:
                new_obj.val += str(other.val)
        elif isinstance(other, int | float):
            new_obj.val += other
        elif isinstance(other, str):
            new_obj.val = str(new_obj.val) + other
        return new_obj

    def __sub__(self, other):
        return self.val - other.val

    def __mul__(self, other):
        return self.val * other.val

    def __truediv__(self, other):
        return self.val / other.val

    def __floordiv__(self, other):
        return self.val // other.val

    # greater than
    def __gt__(self, other):
        return self.val > other.val

    # great or equal
    def __ge__(self, other):
        return self.val >= other.val

    # less than
    def __lt__(self, other):
        return self.val < other.val

    # equal
    def __eq__(self, other):
        return self.val == other.val

    # not equal
    def __ne__(self, other):
        return self.val != other.val


    # Dunder, Magic methods



if __name__ == "__main__":
    object = ExampleClass(5)
    object2 = ExampleClass(15)
    object3 = ExampleClass(7)
    print(object)
    print([object])   # value sifatida "reps" class ishlaydi
    print(bool(object))
    # object.name = 'salom'
    # print(str(object) + str(object2))
    # print(object + 1)
    print(object + object2 + object3 + object + 47 + 15.45)
    print(object + object2 + 1 + object3 + object + 'salom')
    # print(object)
    print(object > object2)
    print(object >= object2)
    print(object < object2)
    print(object == object2)
    print(object != object2)
    print(object / object2)
    print(object // object2)
    print(object - object2)
    print(object * object2)































































# if isinstance(other, ExampleClass):
        #      return self.val + other.val
        # elif isinstance(other, int | float):
        #     return self.val + other



