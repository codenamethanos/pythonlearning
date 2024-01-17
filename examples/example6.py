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
    def bark(self):
        print("bark")
    
class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
