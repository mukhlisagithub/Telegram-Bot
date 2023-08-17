# Masala_2: Laptop nomli class yarating. Unda model, rang nomli private turdagi propertylar bolsin. Getter va setter funksiyalarini tuzib undan
# HP nomli voris class oling. Voris class da getInfo nomli funksiya bolsin. getInfo funksiyasi qiymatlarni getter funksiyasidan olsin. HP dan 2 ta
# object olib ularga qiymatlarni input qiling va getInfo orqali chop eting. Berilgan qiymatlani ozgartirib yangi qiymatlarni ham chop eting.


class Laptop:
    def __init__(self, model, color):
        self.__model = model
        self.__color = color


    @property
    def model(self):
        return self.__model


    @model.setter
    def model(self, val):
        self.__model = val


    @property
    def color(self):
        return self.__color


    @color.setter
    def color(self, val):
        self.__color = val


class HP(Laptop):
    def __init__(self, model, color):
        super().__init__(model, color)


    def getInfo(self):
        return f"Laptop's model is {self.model}, color is {self.color}"

if __name__ == "__main__":
    hp = HP("Asus", "black")
    acer = HP("Lenova", "white")
    print(hp.model)
    print(hp.color)
    print(hp.getInfo())
    print(acer.model)
    print(acer.color)
    print(acer.getInfo())

    hp.model = "Asus"
    print(hp.model)
    hp.color = "grey"
    print(hp.color)
    print(hp.getInfo())

    acer.model = "Mac"
    print(acer.model)
    acer.color = "blue"
    print(acer.color)
    print(acer.getInfo())
