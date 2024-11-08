# Inheritance becomes handy especially when we have many related classes
# Inheritance is a fundamental concept in oop that allows a class (Child class or subclass) to
# take up both the properties(attributes) and methods(4_functions) from another class the
# superclass or parent class.

# There are three basic types of inheritance: Single inheritance: This is when a child class
# inherits from one parent class
# and
# multilevel inheritance: This is when a child class inherits from a parent which also inherits
# from another parent

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} woofs")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} mews")


dog = Dog("Favee")
cat = Cat("Pussy")
dog.speak()
cat.speak()
dog.sleep()
