# The @property decorator in Python is a way to define methods that can be accessed like
# attributes. It allows you to control access to private or internal variables while using a
# more convenient attribute-like syntax. This is particularly helpful in enforcing encapsulation,
# as it lets you add logic to get, set, or delete a property without changing the way the
# property is accessed from the outside.)

class Rectangle:
    def __init__(self, width, height):
        self._width = width  # using underscore to denote it as 'protected'
        self._height = height

    # Getter for width
    @property
    def width(self):
        return self._width

    # Setter for width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = value

    # Getter for height
    @property
    def height(self):
        return self._height

    # Setter for height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = value

    # Property to calculate area
    @property
    def area(self):
        return self._width * self._height

    # Property to calculate perimeter
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


# ##### Basic Use Cases

# Creating a rectangle instance
rect = Rectangle(4, 5)

# Accessing width and height like attributes
print("Width:", rect.width)  # Output: Width: 4
print("Height:", rect.height)  # Output: Height: 5

# Calculating area and perimeter using properties
print("Area:", rect.area)  # Output: Area: 20
print("Perimeter:", rect.perimeter)  # Output: Perimeter: 18

# Setting new values with validation
rect.width = 7
print("Updated Width:", rect.width)  # Output: Updated Width: 7

# Attempting to set an invalid width
# rect.width = -3  # Raises ValueError: Width must be a positive number
