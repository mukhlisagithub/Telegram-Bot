from time import sleep
from os import system

class Person:
    def __init__(self, name, age, phone_number=None):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def sayAge(self):
        sleep(2)
        return f'I\'m {self.age} years old!'
    def say(self):
        sleep(2)
        return f'Hello, my name is {self.name}'

    def compare(self,age):
        sleep(2)
        res = f'I\'m {self.age} years old!\n'
        if self.age > age:
            return res + 'I\'m older than you!'
        elif self.age < age:
            return res + 'I\'m younger than you!'
        else:
            return res + 'We are on the same age!'

    def __str__(self):
        sleep(2)
        if self.phone_number is not None:
            return f'My phone number is {self.phone_number}'
        return 'I don\'t use mobile phone!'

def typing(old_text,text,space=''):
    for i in range(1,len(text)+1):
        system('clear')
        print(old_text,end='')
        print(space+text[0:i])
        sleep(0.1)
    return f'{old_text}{space}{text}\n'

if __name__ == '__main__':
    space = ' '*15
    person1 = Person('Asadbek', 18)
    person2 = Person('Abdulhay',25, '+998905000005')
    old_text = ''
    old_text = typing(old_text,person1.say())
    old_text = typing(old_text,person2.say(),space)
    old_text = typing(old_text,'How old are you?')
    old_text = typing(old_text,person2.sayAge(),space)
    old_text = typing(old_text,person1.compare(person2.age))
    old_text = typing(old_text,'What is your phone number?',space)
    old_text = typing(old_text,str(person1))
    old_text = typing(old_text,'What is your phone number?')
    old_text = typing(old_text,str(person2),space)