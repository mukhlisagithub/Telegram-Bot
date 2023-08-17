from english_words import get_english_words_set
#
# data = get_english_words_set(['web2'], lower=True)
#
# print(data)


from abc import ABC,abstractmethod
import random

class Game(ABC):
    def __init__(self):
        self.scores = 0

    @abstractmethod
    def Start(self):
        return 'Enter your name?'

    @abstractmethod
    def isFinished(self):
        pass


class Easy(Game):
    def __init__(self):
        super().__init__()

    def Start(self):
        print("What is your name? ")
        print("Easy level. ")
        word = random.choice(("get_english_words_set(['web2'], lower=True)"))
        self.play(word, 6)

    def isFinished(self):
        return False


    def play(self, word, max_attempts):
        attempts = 0
        guessed_letters = []

        while attempts < max_attempts:
            guess = input("Enter a letter: ")

            if guess in word:
                print("Correct guess!")
                guessed_letters.append(guess)
                if len(guessed_letters) == len(set(word)):
                    print("Word is found!", word)
                    self.scores += 1
                    break
            else:
                print("Wrong guess!")
                attempts += 1

            print("Guessed letters:", guessed_letters)

        if attempts == max_attempts:
            print("More attempts. Game over.")




class Medium(Easy):
    def __init__(self):
        super().__init__()


    def Start(self):
        print('Medium level.')
        word = random.choice(("get_english_words_set(['web2'], lower=True)"))
        while len(word) > 9:
            word = random.choice(("get_english_words_set(['web2'], lower =True)"))
        self.play(word, 9)

    def isFinished(self):
        return False






class Hard(Medium):
    def __init__(self):
        super().__init__()

    def start(self):
        print("Hard level selected.")
        word = random.choice(("get_english_words_set(['web2'], lower=True)"))
        while len(word) <= 9:
            word = random.choice(("get_english_words_set(['web2'], lower=True)"))
        self.play(word, 9)

    def isFinished(self):
        return True



game1 = Easy()
game1.Start()

# game2 = Medium()
# game2.Start()

# game3 = Hard()
# game3.Start()






# word = 'laptop'
# secret = ['_']*len(word)
# print(*secret)


