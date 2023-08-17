# Masala:  'Animal' nomli super class yarating. Unda 'name' and 'species' nomli attributlar bolsin. Keyin bu class dan 2 ta 'Dog' va 'Cat'
# nomli child classlar yaratib, har bir classning 'sound' nomli metodlari bolsin. Har bir child class larning konstructorlaridan turib, s
# uper class konstructoriga 2 tadan attributlar yuborib, ulardan objectlar olib ishlating.


# ustoz yechbergan usullari:

class Animal:
    def __int__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    # def __init__(self, name, species):  # agar yangi attribut bolsa alohida yozib oladini qolgani super classga otadi
        # super().__init__(name, species)  # superdagi kontructor hamma narsani qiloladi
        # self.color = color

    def make_sound(self):
        return 'Woof - Woof'


if __name__ == "__main__":
    dog = Dog()
    print(dog.make_sound())
    # print(dog.name, dog.species)

