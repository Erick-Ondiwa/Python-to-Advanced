# Lists - this is a collection of multiple items in a single variable. The items in a list can
# either be of the same or different data types
# A list is like an array in other programming languages
# There are two categories of lists: Single dimensional and multi-dimensional lists

# Python List Operations

# In Python, a list is a collection of items that are ordered, changeable, and allow duplicate
# values. Lists are created using square brackets and can contain items of any data type

# Creating a List

# You can create a list by placing elements inside square brackets [], separated by commas.
# Here's an example of creating a list with three integer elements:

ages = [19, 26, 29]
print(ages)  # Output: [19, 26, 29]

# Accessing List Elements

# List items are indexed with the first item having an index of [0]. You can access list elements
# using these indices. For example:

languages = ['Python', 'Swift', 'C++']
print(languages[0]) # Output: Python
print(languages[-1]) # Output: C++

# Adding Elements to a List

# You can add elements to a list using methods like append(), insert(), and extend()

# Using append():
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)
# Output: ['apple', 'banana', 'cherry', 'orange']

# Using insert():
fruits.insert(1, 'blueberry')
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange']

# Using extend():
more_fruits = ['pineapple', 'mango']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'pineapple', 'mango']

# Removing Elements from a List

# To remove elements from a list, you can use methods like remove(), pop(), or the del statement

# Using remove():
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange', 'pineapple', 'mango']

# Using pop():
fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry', 'orange', 'pineapple','mango']

# Using del statement:
del fruits[0]
print(fruits)  # Output: ['cherry', 'orange', 'pineapple','mango']

# Slicing a List

# Slicing allows you to get a sublist by specifying a start and end index. For example:

print(fruits[1:3]) # Output: ['orange', 'pineapple']

# List Comprehension

# List comprehension is a concise way to create lists. It consists of brackets containing an
# expression followed by a for clause.

squared_numbers = [x**2 for x in range(10)]
print(squared_numbers) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# #########CONTINUED#########

fav_foods = ["pizza", "hotdog", "cake"]
for fav_food in fav_foods:
    print(fav_food, end=" ")

foods = {"drinks": ["soda", "Coffee", "Tea"],
         "dinner": ["Pizza", "Hamburger", "Hotdog"],
         "desert": ["Cake", "ice crem"]
         }
foods["drinks"].insert(1, "Chocolate")
print(foods["drinks"])
for values in foods["drinks"]:
    print(values, end=" ")
for key in foods:
    print(key)
# drinks = foods["dinner"][1]
# print(drinks)
# for drinks in foods["drinks"]:
#     print(drinks, end=" ")
# print()
# for key, values in foods.items():
#     for value in values:
#         print(value, end=" ")
#     print()
#
# for food in foods:
#     print(food)
