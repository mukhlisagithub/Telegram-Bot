# Masala_1: Mashina nomli clas yarating. Unda model, rang nomli private turdagi propertylar bolsin. Getter va setter funksiyalarini tuzib undan
# SportCar nomli voris class oling. Voris class da getInfo nomli funkisya bolsin. getInfo funksiyasi qiymatlarini getter funksiyalaridan olsin.
# SportCar dan 2 ta object olib ularga qiymatlarni input qilin va getInfo orqali chop eting. Berilgan qiymatlarini ozgartirib yangi qiymatlarni ham
# chop eting.


class Mashina:
    def __init__(self, model, rang):
        self._model = model
        self._rang = rang


    @property
    def model(self):
        return self._model


    @model.setter
    def model(self, val):
        self._model = val


    @property
    def rang(self):
        return self._rang


    @rang.setter
    def rang(self, val):
        self._rang = val


class SportCar(Mashina):
    def __init__(self, model, rang):
        super().__init__(model, rang)

    def getInfo(self):
        return f"Mashinaning modeli {self.model}, rangi {self.rang}"


if __name__ == "__main__":
    bmw = SportCar("Daewa", "Qizil")
    malibu = SportCar("Chevrolet", "Oq")
    print(bmw.model)
    print(bmw.rang)
    print(malibu.model)
    print(malibu.rang)
    print(bmw.getInfo())
    print(malibu.getInfo())

    bmw.model = "KIA"
    print(bmw.model)
    bmw.rang = "Qora"
    print(bmw.rang)
    print(bmw.getInfo())

    malibu.model = "Toyota"
    print(malibu.model)
    malibu.rang = "Sariq"
    print(malibu.rang)
    print(malibu.getInfo())



