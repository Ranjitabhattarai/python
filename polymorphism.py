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
