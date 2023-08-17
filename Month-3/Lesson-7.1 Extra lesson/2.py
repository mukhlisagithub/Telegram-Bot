class Animal:
    def __init__(self, name):
        self.name = name
        self.check = "Animal Classdan"

    def song(self):
        print("Any song")



class Herbivore(Animal):
    def __init__(self, name):  # palimarfizm sodir bolgan
        self.name = name
        self.check = "Herbivore Classdan"


    def song(self):
        print("Any herbivore song")

    def song(self, ovoz):
        print(self.name, ovoz)





dog = Animal("REX")
print(dog.name)
dog.song()
print(dog.check)

rabbit = Herbivore("MAX")
print(rabbit.name)
rabbit.song("G'it-g'it")
print(rabbit.check)   # qaysi classdanligi aniqlab beradi
