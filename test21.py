# INHERITENCE
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    # pass
    # pass keyword is used when we do not want to add any other properties or methods to the class
    
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
