# A tuple is one of the four data structures in python. They are used to store multiple items in a
# single variable and are written with round brackets.Tuples are characterized by being ordered
# and unchangeable, meaning that once a tuple is created, its items cannot be modified.

# Creating and Using Tuples

# To create a tuple, you can simply enclose the items within parentheses. For example:

mytuple = ("apple", "banana", "cherry")
print(mytuple)

# If you need to create a tuple with only one item, you must include a comma after the item,
# otherwise, it will not be recognized as a tuple:

# Correct way to create a single item tuple
single_item_tuple = ("apple",)

# Incorrect, this is not a tuple
not_a_tuple = ("apple")

# Tuples can contain items of any data type and can even contain a mix of different types:

tuple1 = ("abc", 34, True, 40, "male")

# Tuple Characteristics

# Ordered: The items in a tuple have a specific order that will not change.

# Unchangeable: Once a tuple is created, you cannot change, add, or remove items.

# Allow Duplicates: Tuples can have items with (the) same value, which means they can contain
# duplicates.

# Indexing: Each item in a tuple has an index, starting from 0.

# Accessing Tuple Items

# You can access tuple items by referring to the index number:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # Outputs "banana"

# Negative indexing means starting from the end of the tuple:

print(thistuple[-1]) # Outputs "cherry"

# Immutability of Tuples

# Tuples are immutable, which means that you cannot change tuple items after the tuple has been
# created. Attempting to do so will result in a TypeError:

thistuple[1] = "strawberry" # Raises a TypeError

# Tuple Length

# To determine the number of items in a tuple, use the len() function:

print(len(thistuple)) # Outputs 3

# Tuple Operations

# Tuples support various operations like concatenation, nesting, repetition, and slicing. For
# instance, you can concatenate tuples using the + operator:

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2) # Outputs (1, 2, 3, 4, 5, 6)

# Converting Between Tuples and Other Types

# You can convert a tuple to a list to modify it, and then convert it back to a tuple:

mylist = list(mytuple)
mylist.append("orange")
mytuple = tuple(mylist)
