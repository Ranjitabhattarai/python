class Animal:
    def speak(self):
      pass
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Puppy(Animal):
    def speak(self):
        return "bark!"

animals = [Dog(), Cat(), Puppy()]
for animal in animals:
    print(animal.speak())

#abstraction
from abc import ABC, abstractmethod

class Greet(ABC):

    @abstractmethod
    def say_hello(self):
        pass                #abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())
