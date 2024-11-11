# Polymorphism in Python allows different objects to be treated as instances of the same class
# through a common interface. It enables objects from different classes to respond to the same
# method call, fostering code flexibility and reuse. In Python, polymorphism is implemented
# through method overriding and duck typing. Here’s a practical example to illustrate this concept.

import math


class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self, color):
        self.color = color
        print(f"Drawing a {self.color} {self.name}")

    def area(self):
        raise NotImplementedError("Subclass must implement area method")


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)  # Using super() to initialize the name
        self.radius = radius

    def draw(self, color):
        super().draw(color)  # Call the common draw functionality
        print(f" with radius {self.radius}")

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)  # Using super() to initialize the name
        self.width = width
        self.height = height

    def draw(self, color):
        super().draw(color)  # Call the common draw functionality
        print(f" with width {self.width} and height {self.height}")

    def area(self):
        return self.width * self.height


# Create instances and draw them
shapes = [Circle(name='Circle', radius=5), Rectangle(name='Rectangle', width=6, height=10)]

for shape in shapes:
    shape.draw("blue")  # Passing color parameter to the draw method
    print(f"Area: {shape.area()}\n")  # Calling the area method specific to each shape
