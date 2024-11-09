# The enumerate() function in Python is a built-in function that allows you to iterate over an
# iterable (such as a list, tuple, or string) while also keeping track of the current index (
# position) in the iterable. It essentially adds a counter to an iterable and returns it as an
# enumerate object, which can be used to iterate over both the index and the value at the same time.
from numpy import concat
from numpy._core.defchararray import lower
from numpy._core.strings import upper

# Syntax:
iterable = ""
enumerate(iterable, start=0)

# Parameters:
# iterable: The sequence (list, tuple, string, etc.) that you want to iterate over.
# start (optional): The starting index for the enumeration. By default, it starts from 0,
# but you can specify a different start index if needed.
# Return Value:
# The enumerate() function returns an enumerate object, which yields pairs of index and
# corresponding elements from the iterable.

# Example 1: Basic Usage of enumerate()
# Let’s look at a simple example where we iterate over a list and print each item along with its
# index.

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Here, the enumerate() function allows us to access both the index (0, 1, 2) and the
# corresponding value ('apple', 'banana', 'cherry') in a single iteration.

# Example 2: Changing the Start Index
# You can use the start parameter to change the starting index. For example, you can start
# counting from 1 instead of 0.

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# In this case, the enumeration starts from 1 instead of 0.

# Example 3: Enumerating Over a String
# You can use enumerate() to iterate over individual characters of a string, along with their
# positions.

word = "hello"

for index, letter in enumerate(word):
    print(index, letter)

# This shows how enumerate() can be used with strings to keep track of the index of each character.

# Example 4: Using enumerate() with Lists in List Comprehensions
# You can use enumerate() within list comprehensions to build new lists based on both the index
# and the value of each element.

numbers = [10, 20, 30, 40]

# Create a list of strings indicating the position and the value
indexed_numbers = [f"Index {i}: {num}" for i, num in enumerate(numbers)]
print(indexed_numbers)

# Here, enumerate() helps us easily construct a list of strings that include both the index and
# the value.

# Example 5: Enumerating Over Multiple Lists
# You can combine enumerate() with zip() to iterate over multiple lists, while also keeping track
# of the index.

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"Student {i}: {name} scored {score}")

# In this example, enumerate() is used to track the student number, while zip() pairs the names
# and scores lists.

# Example 6: Enumerating a Tuple
# The enumerate() function works with any iterable, including tuples.

colors = ('red', 'green', 'blue')

for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# Example 7: Modifying Items in a List Using enumerate()
# If you need to modify items in a list based on their index, enumerate() makes it easy to
# reference both the index and the value.

numbers = [10, 20, 30, 40]

# Increment every number at an odd index by 5
for i, num in enumerate(numbers):
    if i % 2 != 0:
        numbers[i] += 5

print(numbers)

# In this case, we used the index provided by enumerate() to modify only the items at odd indices.

# Example 8: Enumerate with a Dictionary
# Although enumerate() cannot be directly applied to a dictionary, you can still use it with
# dict.items() to enumerate both the keys and values of the dictionary.

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

for i, (key, value) in enumerate(person.items(), start=1):
    print(f"Pair {i}: {key} = {value}")

# Example 9: Flattening Enumerated List of Lists
# You can use enumerate() when you have a list of lists, and you need both the outer list index and
# the inner list index.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"Element at row {i}, col {j}: {val}")

# Example 10: Enumerating to Handle Errors
# You can use enumerate() to help with debugging by including the index in your error messages or
# logs.

items = [10, 'twenty', 30]

for i, item in enumerate(items):
    try:
        result = item + 1  # This will cause an error for the string 'twenty'
    except TypeError as e:
        print(f"Error at index {i}: {e}")

# This can be a helpful debugging technique when working with large datasets or lists with mixed
# data types.

# Conclusion:
# The enumerate() function is a powerful tool for looping through an iterable while keeping track
# of the index.
# It is useful when you need both the index and the element in loops, especially when modifying
# data or creating new collections based on indices.
# You can combine enumerate() with other 3_functions like zip() or dict.items() to achieve more
# complex iteration tasks.
# The start parameter gives you control over where to begin the index, providing flexibility when
# working with enumerations.


# ************************* EXERCISE USING enumerate() FUNCTION ************************************
# #1 You are given a list of student names. Write a program to print each student's name along
# with their index, starting from 1

stu_names = ["Erick Ondiwa", "James Wasonga", "Felix Awere", "Shadrack Mutinda", "Mark Emmanuel"]
for idx, stu_name in enumerate(stu_names, start=1):
    print(f"{idx}. {stu_name}")

# #2 You are given a list of numbers. Write a program that increments every number located at an
# even index by 2.

numbers = [3, 4, 7, 12, 17, 20, 26, 41, 50]
for even_idx, number in enumerate(numbers):
    if even_idx % 2 == 0:
        number += 2
        print(number)
    # if numbers[even_idx] % 2 == 0:
    #

# #3 You are given a list of words. Write a program that prints out all the words that are
# located at an odd index in the list.

vocabularies = ["patience", "kindness", "tolerance", "trustworthy", "adaptability"]
for voc_idx, vocabulary in enumerate(vocabularies):
    if voc_idx % 2 != 0:
        print(f"{voc_idx}. {vocabulary}")

# #4You are given a list of cities. Create a dictionary where the keys are the indices of the
# cities (starting from 1) and the values are the city names.

kenya_cities = ["Nairobi", "Kisumu", "Mombasa", "Nakuru", "Migori"]
for city_idx, kenya_city in enumerate(kenya_cities):
    print(f"{city_idx}. {kenya_city}")

# #5 Given a 2D list (matrix), write a program that prints the index of each element in the matrix
# along with its value.

list_of_ints = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for int_idx, list_of_int in enumerate(list_of_ints):
    for int_index, ints in enumerate(list_of_int):
        print(f"Row {int_idx} Column {int_idx}: {ints}")

# #6 You are given a list of temperatures recorded over a week. If the temperature is found to be
# less than 10°C, increase it by 5°C. Use the index to check which temperatures should be adjusted.

weekly_temps = [12, 7, 9, 15, 6, 18, 20]

for temp_idx, weekly_temp in enumerate(weekly_temps):
    if weekly_temps[temp_idx] < 10:
        weekly_temp += 5
    print(f"{temp_idx}. {weekly_temp}")

# #7 You are given a string of lowercase letters. Write a program to capitalize every letter
# located at an odd index.

group_name = "codecrafter"
for letter_idx, each_letter in enumerate(group_name):
    if letter_idx % 2 != 0:
        each_letter = upper(each_letter)
    # print(each_letter, end="")

erick_description = "eRicKondiWathEcoDeCraFteR.Ke"
for letter_index, every_letter in enumerate(erick_description):
    if erick_description[letter_index].isupper():
        every_letter = lower(every_letter)
    elif erick_description[letter_index].islower():
        every_letter = upper(every_letter)
    else:
        print(every_letter, end="")
    print(every_letter, end="")

# #8 You have a list of tuples containing movie names and their release years. Write a program to
# print each movie's name along with its release year and its index in the list, starting from 1.


movie_details = [("Inception", 2010), ("The Matrix", 1999), ("Interstellar", 2014)]
for movie_idx, movie_detail in enumerate(movie_details):
    print(movie_detail)


class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


rocket1 = Rocket(3, 4)
print(rocket1.x)
