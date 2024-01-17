class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hello, my name is {self.name}")

person1 = Person('Nifal')
person1.say_hi()


class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

dog1 = Dog()
dog1.walk()