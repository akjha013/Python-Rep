# modules
import test20


class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    # pass
    def bark(self):
        print('bark')

class Cat(Mammal):
    def meow(self):
        print('meow')


dog = Dog()
dog.walk()
dog.bark()
cat = Cat()
cat.walk()
cat.meow()
test20.Person('Kevin Malone').talk()
