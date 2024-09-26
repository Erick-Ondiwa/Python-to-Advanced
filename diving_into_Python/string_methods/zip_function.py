# The zip() function in Python is a useful tool that allows you to combine multiple iterables (
# such as lists, tuples, etc.) element-wise. It pairs elements from the provided iterables into
# tuples, effectively "zipping" them together. The result is an iterator of tuples, where each
# tuple contains one element from each iterable.

# Syntax:
iterables = ""
zip(*iterables)
# Parameters:
# iterables: Any number of iterable objects (e.g., lists, tuples, strings) that you want to zip
# together.
# Return Value:
# The zip() function returns an iterator of tuples, with each tuple containing elements from the
# corresponding positions in all iterables.

# Example 1: Zipping Two Lists

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = zip(list1, list2)
print(result)  # this will print the memory address of the result
# print(list(result))  # Converting the zip object to a list to see the result

# Output:
output1 = [(1, 'a'), (2, 'b'), (3, 'c')]
# Here, the first elements of list1 and list2 are paired together, the second elements are paired,
# and so on.

# Example 2: Zipping Three Iterables
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']

result = zip(numbers, letters, symbols)
# print(list(result))
# Output:
output2 = [(1, 'a', '!'), (2, 'b', '@'), (3, 'c', '#')]
# In this case, each tuple contains one element from each iterable (numbers, letters, and symbols).

# Example 3: Handling Iterables of Different Lengths
# If the iterables have different lengths, zip() stops creating pairs when the shortest iterable
# is exhausted.

numbers = [1, 2, 3, 4]
letters = ['a', 'b']

result = zip(numbers, letters)
# # print(list(result))

# Output:
output3 = [(1, 'a'), (2, 'b')]
# Notice how zip() only paired the first two elements, since letters has only two elements.

# Example 4: Unzipping with zip()
# You can also "unzip" a list of tuples back into separate lists using the zip() function with the
# unpacking operator *.

zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*zipped)
# print(numbers)
# print(letters)

# Output:
output4a = (1, 2, 3)
output4b = ('a', 'b', 'c')
# Here, the *zipped unpacks the zipped list into two separate iterables: one for numbers and one
# for letters.

# Example 5: Zipping Strings
# Since strings are also iterables, you can use zip() to combine characters from multiple strings.

str1 = "ABC"
str2 = "123"

result = zip(str1, str2)
# print(list(result))

# Output:
output5 = [('A', '1'), ('B', '2'), ('C', '3')]

# Example 6: Using zip() in a Loop
# You can loop through the zipped values directly, which is handy for iterating through multiple
# sequences at once.

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")


# This is useful for situations like pairing students with their scores or combining parallel
# lists for processing.

# Example 7: Zipping with Enumerate
# You can combine zip() with enumerate() to get both index and value pairs from two lists.

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for i, (name, score) in enumerate(zip(names, scores)):
    print(f"Student {i}: {name} scored {score}")

# Performance Notes:
# Iterator Efficiency: The zip() function returns an iterator, meaning that it does not generate
# the full list of paired elements all at once. Instead, it generates them on demand, making it
# efficient for large datasets.
# Lazy Evaluation: Because zip() returns an iterator, it only computes the values when you iterate
# over it. If you need a list of the results, you must convert it using list().


# *************** ADVANCED USES OF THE zip() FUNCTION *****************

# 1. Zipping Multiple Lists and Summing Corresponding Elements
# In this example, we'll combine several lists of numbers and sum the elements at corresponding
# positions.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Use zip to pair corresponding elements
summed = [a + b + c for a, b, c in zip(list1, list2, list3)]
# print(summed)

# Here, each element in the resulting list is the sum of the corresponding elements from list1,
# list2, and list3.

# 2. Zipping Dictionaries by Keys
# You can zip together two dictionaries by zipping their keys or values. For instance, let's pair
# the keys and values from two different dictionaries.

dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'name': 'Bob', 'age': 30}

# Zipping by keys
for (key1, value1), (key2, value2) in zip(dict1.items(), dict2.items()):
    print(f"{key1} from dict1: {value1}, {key2} from dict2: {value2}")

# 3. Pairing Lists of Unequal Lengths Using itertools.zip_longest()
# If you need to zip iterables of different lengths and don’t want to lose any data,
# use the itertools.zip_longest() function  which fills the shorter lists with a specified value
# (default is None).

from itertools import zip_longest

list1 = [1, 2]
list2 = ['a', 'b', 'c']

# Zipping using zip_longest with a fill value
result = zip_longest(list1, list2, fillvalue='empty')
# print(list(result))

# In this case, the shorter list (list1) was filled with 'empty' for the missing element.

# 4. Zipping with Filtering: Combining Even and Odd Indexes
# Let’s say you have a list, and you want to create two new lists: one with elements at even
# indices and another with elements at odd indices. You can use zip() to combine these lists
# efficiently.

numbers = [1, 2, 3, 4, 5, 6]

# Separate even-indexed and odd-indexed elements
evens = numbers[::2]  # Elements at even indices
odds = numbers[1::2]  # Elements at odd indices

# Pair the even and odd indexed elements
paired = list(zip(evens, odds))
# print(paired)

# 5. Sorting Using zip()
# You can use zip() to sort one list based on another. For example, if you have a list of names
# and corresponding scores, you can sort the names based on the scores.

names = ['Charlie', 'Alice', 'Bob']
scores = [90, 85, 95]

# Sort names based on scores
sorted_pairs = sorted(zip(scores, names), reverse=True)  # Sort by score, descending
sorted_scores, sorted_names = zip(*sorted_pairs)

print(f"Sorted names: {sorted_names}")
print(f"Sorted scores: {sorted_scores}")

# Here, zip() pairs scores with names, sorts the pairs by score, and then unzips them back into
# two sorted lists.

# 6. Transposing a Matrix Using zip()
# You can use zip() to transpose a matrix (swap rows and columns). This is a common task in
# numerical computing.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose the matrix using zip
transposed = list(zip(*matrix))
# print(transposed)

# Here, the rows of the original matrix are turned into columns using zip(*matrix).

# 7. Merging Two Lists into a Dictionary
# You can combine two lists (one for keys and one for values) into a dictionary using zip().

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Create a dictionary from two lists
merged_dict = dict(zip(keys, values))
# print(merged_dict)

# 8. Iterating Over Multiple Sequences Simultaneously
# When you have multiple lists of related data (e.g., names, ages, and cities), you can iterate
# over them together using zip().

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'Los Angeles', 'Chicago']

# Iterating over multiple sequences simultaneously
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}.")
