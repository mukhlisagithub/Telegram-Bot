# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
        # Encapsulation - Data hiding
        # restricting access to the attributes => murojaatni cheklash


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self._Base__c)

    def p(self):
        print("Calling private member of base class: ")
        print(self.__c)



new_obj = Base()
print(new_obj.a)
print(new_obj._Base__c)

# Driver code
# obj1 = Derived()
# print(obj1.a)
# print(obj1.p)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class