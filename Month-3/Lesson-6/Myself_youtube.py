# class Animal:
#
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")
#
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
#
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()




# Task-2 for me
# Inheritance in Python

# Agenda:
# What is Inheritance?
# Init Function
# Types of Inheritance with example
# Python Super Function
# Method Overriding


# What is Inheritance?:
class Parent:
    def func1(self):
        print("This is a parent function")


class Child(Parent):
    def func2(self):
        print("This is a child function")


ob = Child()
ob.func1()
ob.func2()


# Init Function
# __init__() function is called automatically every time the class is used to create an object

class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "mukhlisa"

    def view(self):
        print(self.age, self.lastname, self.name)

ob = Child(23, 'python')
ob.view()



# Types of Inheritance with example: SINGLE, MULTIPE, MULTILEVEL, HIERARCHICAL, HYBRID

# single inheritance: => When the inheritance involves one child class and one parent class
# multiple inheritance: => It involves more than one parent class
# multilevel: => The child class acts as a parent class for another child class
# hierarchical inheritance: => More than one type of inheritance


# Single inheritance:
class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        print("This is function 2")


ob = Child()
ob.func1()



# Multiple inheritance:
class Parent:
    def func1(self):
        print("This is function 1")

class Parent2:
    def func3(self):
        print("This is function 3")

class Child(Parent, Parent2):
    def func2(self):
        print("This is function 2")


ob = Child()
ob.func1()
ob.func3()



# Multilevel inheritance:
class Parent:
    def func1(self):
        print("This is function 1")


class Parent2(Parent):
    def func3(self):
        print("This is function 3")

class Child(Parent2):
    def func2(self):
        print("This is function 2")

ob = Child()
ob.func1()
ob.func3()



# hierarchical inheritance:
class Parent:
    def func1(self):
        print("This is function 1")


class Parent2(Parent):
    def func3(self):
        print("This is function 3")


class Child(Parent):
    def func2(self):
        print("This is function 2")


ob = Child()
ob1 = Parent2()
ob.func1()
ob1.func1()



# Hybrid inheritance:
class Parent:
    def func1(self):
        print("This is function 1")


class Parent2(Parent):
    def func3(self):
        print("This is function 3")


class Parent3:
    def func4(self):
        print("This is function 4")


class Child(Parent, Parent3):
    def func2(self):
        print("This is function 2")


ob = Child()
ob.func1()
ob.func4()




# Python Super Function: super function directly calls the parent class method
class Parent:
    def func1(self):
        print("This is function 1")

class Child(Parent):
    def func2(self):
        super().func1()
        print("This is function 2")


ob = Child()
ob.func2()



# Method Overriding: Method overriding can be achieved to change functionality of parent class function:
class Parent:
    def func1(self):
        print("This is function 1")


class Child(Parent):
    def func1(self):
        print("This is function 2")


ob = Child()
ob.func1()