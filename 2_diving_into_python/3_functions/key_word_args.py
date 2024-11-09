# Understanding Keyword Arguments in Python

# In Python, keyword arguments allow you to pass values to a function with a key-value syntax,
# where the key is the parameter name within the function. This method provides clarity and
# flexibility in function calls, as the order of the arguments does not impact the outcome.

# Code Example with Keyword Arguments

# Consider a function that requires two parameters, name and age. Using keyword arguments,
# you can call this function by explicitly stating which value corresponds to which parameter,
# like so:

def name_age(name, age):
    print(f"Hi, I am {name}")
    print(f"My age is {age}")

# Using keyword arguments


name_age(name="Alice", age=30)
name_age(age=30, name="Alice")

# In both calls, the output will be the same because the arguments are associated with their
# respective parameter names, regardless of their order.

# Benefits of Keyword Arguments

# The primary advantage of using keyword arguments is the reduction of errors related to argument
# order. This is particularly useful when dealing with 3_functions that have many parameters or
# when the order of parameters is not intuitive. By specifying arguments by name, you ensure that
# each value is assigned to the correct parameter, leading to more readable and maintainable code.

# Positional vs. Keyword Arguments

# While positional arguments are passed in the order defined by the function's parameters,
# keyword arguments free you from this constraint. Positional arguments can lead to unexpected
# results if the order is incorrect, as demonstrated in the following example:


def name_age(name, age):
    print(f"Hi, I am {name}")
    print(f"My age is {age}")

# Positional arguments


name_age("Bob", 25)  # Correct order
name_age(25, "Bob")  # Incorrect order, leads to a logical error

# In the second call, the age is printed as the name and vice versa, which is not the intended
# behavior.
