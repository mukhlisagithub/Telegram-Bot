# Abstract Base Class
from abc import ABC,abstractmethod, abstractproperty
from sys import getsizeof

# function => funksiyani nomi bn chaqirsa boladi
# method => biron narsani davomidan kn nuqta qoyib chaqiriladigan narsalae:
# a = []
# a.append()  # methodlar
# https://docs.python.org/3.10/library/abc.html#abc.ABCMeta

# Abstarct class: class yaratib qoyib inherit qlb olingan qilgandaga barcha classlarning ichki qismida majburiy yozilishi kerak bolgan funkisya va propertylarni oldindan elon qilib qoyish

class AbstractUser(ABC):
    # no constructors => konstructorlar bomedi abstruct clasda
    # empty abstract methods => metodlari ham bolmaydi
    # declaring with decorator => decoratorlar yordamida chaqiriladi (getter and setter) metodlar "@" belgi orqali chaqiriladi

    @abstractproperty
    def fullname(self):
        pass

    @abstractmethod
    def typing(self):
        pass

class User(AbstractUser):
    __slots__ = ('_fullname', 'age')  # metod nomi, slot ishlagan vaqti dict ishlamaydi

    def __init__(self, name):
        self._fullname = name
        self.age = 15

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, val):
        self._fullname = val


    def typing(self):
        return f'Hello, my name is {self.fullname}'


if __name__ == "__main__":
    # obj = AbstractUser()  # obyekti bomaydi abstract classlarni bular shablon hisoblanadi
    user1 = User('Hakimov Rustam')
    print(user1.fullname)
    user1.fullname = 'Hakimov Raxmon'
    print(user1.typing())
    # print(user1.__dict__)  # dictionary korinishida chqrb beradi
    print(user1.__slots__)
    user1.age = 10
    # print(user1.__dict__)
    print(user1.__slots__)
    user2 = User('')
    # print(user2.__dict__)  # faqat fullname metodi chqadi consolega
    print(user2.__slots__)
    print(getsizeof(User))  # xotiradan qancha joy olganligi
