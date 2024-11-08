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

# A. Adding Elements to a List

# You can add elements to a list using methods like append(), insert(), and extend()

# Using 1. append(item): Adds an item to the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)
# Output: ['apple', 'banana', 'cherry', 'orange']

# Using 3.insert(index, item): Inserts an item at a specified index, shifting items to the right.

fruits.insert(1, 'blueberry')
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange']

# Using 2. extend(iterable): Extends the list by appending all elements from the given iterable (
# like a list, tuple, or string).
more_fruits = ['pineapple', 'mango']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'orange', 'pineapple', 'mango']

# B. Removing Elements from a List

# To remove elements from a list, you can use methods like remove(), pop(), or the del statement

# Using 1. remove(item): Removes the first occurrence of an item. Raises a ValueError if the item
# is not found.:
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange', 'pineapple', 'mango']

# Using 2.pop(index): Removes and returns the item at the specified index. If no index is
# specified, it removes and returns the last item:
fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry', 'orange', 'pineapple','mango']

# Using 3. del statement:
del fruits[0]
print(fruits)  # Output: ['cherry', 'orange', 'pineapple','mango']

# 4. clear()
# Removes all elements from the list, making it empty.
fruits.clear()

# #### OTHER METHODS ####
# 7. index(item, start, end):
# Returns the index of the first occurrence of the item between the optional start and end
# positions. Raises a ValueError if the item is not found.

fruits = ['apple', 'banana', 'cherry', 'apple']
print(fruits.index('apple'))        # Output: 0
print(fruits.index('apple', 1))     # Output: 3

# 8. count(item)
# Counts the occurrences of an item in the list.

fruits = ['apple', 'banana', 'cherry', 'apple']
print(fruits.count('apple'))  # Output: 2

# 9. sort(key=None, reverse=False)
# Sorts the list in ascending order by default. The reverse=True parameter sorts it in descending
# order, and the key parameter can be used to specify a custom sorting function.

numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]

# 10. reverse()
# Reverses the order of the list in place.

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

# 11. copy()
# Creates a shallow copy of the list. This is useful when you want to duplicate a list without
# modifying the original.

fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
fruits_copy.append('date')
print(fruits)       # Output: ['apple', 'banana', 'cherry']
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry', 'date']

# 12. len()
# Although not a list method, len() is a built-in function that returns the number of elements in
# a list.

fruits = ['apple', 'banana', 'cherry']
print(len(fruits))  # Output: 3

# #######Examples of Practical Use ######
# Removing Duplicates
# You can use a combination of append() and count() to filter out duplicates.

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)
print(unique_numbers)  # Output: [1, 3, 5]

# Sorting with Custom Key
# Suppose we have a list of words and want to sort them by length.

words = ['apple', 'banana', 'cherry', 'date']
words.sort(key=len)
print(words)  # Output: ['date', 'apple', 'banana', 'cherry']

# Inserting Multiple Elements
# To insert multiple items at a specific position, use slice assignment.

fruits = ['apple', 'cherry']
fruits[1:1] = ['banana', 'date']
print(fruits)  # Output: ['apple', 'banana', 'date', 'cherry']

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
