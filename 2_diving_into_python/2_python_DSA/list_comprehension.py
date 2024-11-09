# List comprehension in Python is a concise way to create lists using a single line of code. It
# consists of an expression followed by a for loop, and can include conditions. List
# comprehensions are often used to transform or filter elements in a list in a readable and
# efficient way.

#   Basic Syntax of List Comprehension

# [expression for item in iterable if condition]

# expression: The item or transformation you want in the new list.
# for item in iterable: Loops over each item in the iterable (e.g., list, range).
# if condition (optional): Applies a filter to include only items that meet this condition.
# Practical Example: Filtering Even Numbers from a List
# Suppose you have a list of numbers, and you want to create a new list containing only th even
# numbers. Without list comprehension, this would look like:

# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a for loop to filter even numbers
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)  # Output: [2, 4, 6, 8, 10]


# Using list comprehension to filter even numbers
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


# More Practical Examples of List Comprehension
#           1.Squaring Numbers in a List

squares = [number ** 2 for number in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#           2.Creating a List of Uppercase Strings

names = ["alice", "bob", "carol"]
upper_names = [name.upper() for name in names]
print(upper_names)  # Output: ['ALICE', 'BOB', 'CAROL']

#           3.Generating a List of Even Numbers Using range()

even_numbers = [n for n in range(1, 21) if n % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#           4.Filtering Names Based on Length

names = ["Anna", "Benjamin", "Cara", "Dave"]
short_names = [name for name in names if len(name) < 5]
print(short_names)  # Output: ['Anna', 'Cara', 'Dave']
