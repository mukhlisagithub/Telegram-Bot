from code2 import Person, typing

obj1 = Person("Sardor", 15, '+998914586923')
text = typing('', obj1.say())
text = typing(text, obj1.sayAge())
text = typing(text, str(obj1))