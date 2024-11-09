#       A.Defining and Assigning Values to Variables
# 1.Integer data types
length = 12
width = 8
area = length * width
print("Area = "+str(area))

# String Data types
name = "Shadrack Muema"
age = 21

print("Your name is " + name + "." + " You are " + str(age) + " years old")

first_name = "Erick"
last_name = "Ondiwa'z"
full_name = first_name + " " + last_name
print("I am "+full_name)
print(len(last_name))

# Formatted Strings
my_name = "Erick Kondiwa"
my_age = 24
print(f"My name is {my_name}. I am {my_age} years old")

# 3. Boolean data types
isOnline = True
if isOnline:
    print("You are online")
else:
    print("You are offline")

# Type Hinting= This means defining a variable by statically stating its type
name: str = "Erick"
age: int = 23
isAttractive: bool = False

print(name)
print(age)
print(isAttractive)

# Multiple Assignments with type hinting
my_string, my_integer, my_float = "Hello, World!", 42, 3.14  # type: str, int, float
print(my_string)
print(my_float)
print(my_integer)

