# Inheritance => vorislik

class A:
    def name(self):
        return 'class name A'


class C:
    def surname(self):
        return 'class name C'


class B(A,C):  # Multiple Inheritance  # Inheritance olinayotgan payti ketma ketlik muhim rol oynaydi qaysi biri birinchi kelgan bolsa usha birinchi bolib consolega chiqadi
    def name(self):
        return A().name()

# Super Class => A and C
# Child Class => B

# obj = A()
obj2 = B()
print(obj2.name())

# print(obj2.surname())


## !!! => djangoga otishdan avval ozingni portfolioyong uchun kichik kichik loyihalaringni qilib qoyaver

















# obj = ClassName() # Instance()