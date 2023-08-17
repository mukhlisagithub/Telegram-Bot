class Mashina:
    def __init__(self, model, rang):
        self._model = model
        self._rang = rang

    def getModel(self):
        return self._model

    def setModel(self, model):
        self._model = model

    def getRang(self):
        return self._rang

    def setRang(self, rang):
        self._rang = rang


class SportCar(Mashina):
    def getInfo(self):
        return f"{self.getModel()} {self.getRang()}"


obj1 = SportCar("BMW", "Black")
obj2 = SportCar("Ferrari", "Yellow")

print(obj1.getInfo())
print(obj2.getInfo())

obj1.setRang("Yellow")
obj2.setModel("Red")

print(obj1.getInfo())
print(obj2.getInfo())


# stdout:
#
# BMW Black
# Ferrari Yellow
# BMW Yellow
# Ferrari Red