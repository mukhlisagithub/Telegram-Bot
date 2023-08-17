# Masala:  'Animal' nomli super class yarating. Unda 'name' and 'species' nomli attributlar bolsin. Keyin bu class dan 2 ta 'Dog' va 'Cat'
# nomli child classlar yaratib, har bir classning 'sound' nomli metodlari bolsin. Har bir child class larning konstructorlaridan turib, s
# uper class konstructoriga 2 tadan attributlar yuborib, ulardan objectlar olib ishlating.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Dog(Animal):
    def sound(self):
        print("This dog is voving")


class Cat(Animal):
    def sound(self):
        print("This cat is meowing")


dog = Dog("Simba", "Busky")
cat = Cat("Mosh", "Famby")

dog.sound()
cat.sound()


