# CONSTRUCTOR IN PYTHON
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'hi I am {self.name}')


prsn = Person('wacko9')
# print(f'person name is {prsn.name}')
prsn.talk()

prsn2 = Person('Jim Halpert')
prsn2.talk()
