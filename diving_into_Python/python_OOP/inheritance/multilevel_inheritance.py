# Multilevel inheritance: This is when a child class inherits from a parent which also inherits
# from another parent

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Pray(Animal):
    def flee(self):
        print(f"{self.name} fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} hunting")


class Rabbit(Pray):
    pass


class Hawk(Predator):
    pass


class Fish(Pray, Predator):
    pass


# rabbit = Rabbit("Apuoyo")
# fish = Fish("Tilapia")
# fish.eat()
# fish.hunt()
# fish.flee()


class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


class Square(Shapes):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def area(self):
        return pow(self.width, 2)


class Triangle(Shapes):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height * 0.5


circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="White", is_filled=True, width=25)
triangle = Triangle(color="blue", is_filled=True, width=10, height=20)

print(f"{square.area()}cm^2")
print(f"{triangle.area()}cm^2")
