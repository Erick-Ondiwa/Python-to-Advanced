# Understanding *args and **kwargs in Python

# In Python, *args and **kwargs are special keyword parameters that allow functions to accept an
# arbitrary number of arguments and keyword arguments respectively. They are used to create more
# flexible code that can handle a varying amount of input values without having to define a
# function for each case.

# Using *args

# The *args parameter allows a function to accept any number of positional arguments. This can be
# particularly useful when the number of inputs a function should accept is not known beforehand.
# The arguments passed to *args are accessible as a tuple within the function.

# Here's an example of a function using *args to sum all the values passed to it:

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4)) # Output: 10

# Using **kwargs

# The **kwargs parameter allows a function to accept any number of keyword arguments. This is
# useful when you want to handle named arguments in a function. The keyword arguments passed to
# **kwargs are accessible as a dictionary within the function.

# Here's an example of a function using **kwargs to print named arguments:

def print_names(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_names(first_name="John", last_name="Doe")

# Combining *args and **kwargs

# Both *args and **kwargs can be used together in a function to accept both positional and keyword
# arguments.

def register_user(*args, **kwargs):
    print(args) # This will print a tuple of positional arguments
    print(kwargs) # This will print a dictionary of keyword arguments

register_user("John", "Doe", age=30, country="USA")

# Unpacking with * and **

# The * and ** operators can also be used to unpack iterables and dictionaries respectively when
# calling a function.

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

user_info = {'first_name': 'Jane', 'last_name': 'Doe'}
greet(**user_info) # Unpacks the dictionary and passes as keyword arguments

# Practical Uses

# *args and **kwargs are particularly useful in function overriding and decorators where the
# arguments to be passed to the original function are not known in advance. They also help in
# creating APIs that are flexible and can handle a variety of input formats.

# In conclusion, *args and **kwargs are powerful tools for creating flexible functions that can
# handle different amounts of arguments and keyword arguments. They are widely used in Python and
# understanding them can greatly enhance your ability to write effective and efficient code

