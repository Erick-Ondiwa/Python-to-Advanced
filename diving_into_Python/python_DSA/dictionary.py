# Understanding Dictionaries in Python

# Dictionaries in Python are a collection of key-value pairs, where each key is associated with a
# value. They are mutable, meaning they can be changed after they are created, and they do not
# allow duplicate keys, ensuring that each key is unique within a dictionary.

# Creating and Using Dictionaries

# To create a dictionary, you can use curly braces {} with key-value pairs separated by commas,
# and a colon : separating each key from its value. Here's an example of a simple dictionary:

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# To access a value in a dictionary, you use the key associated with that value:

print(my_dict["brand"])  # Output: Ford

# If you try to access a key that doesn't exist, Python will raise a KeyError.

# Modifying Dictionaries

# Dictionaries are changeable, so you can add new key-value pairs or change the value associated
# with an existing key:

my_dict["color"] = "red" # Adds a new key-value pair
my_dict["year"] = 2020 # Updates the value for the "year" key

# To remove a key-value pair, you can use the del statement:

del my_dict["model"] # Removes the key "model" and its associated value

# Dictionary Methods

# Python dictionaries have a variety of methods that allow you to work with them effectively:

# dict.clear(): Empties the dictionary.

# dict.get(key): Returns the value for the specified key, or None if the key is not found.

# dict.items(): Returns a view object with key-value pairs as tuples.

# dict.keys(): Returns a view object with all the keys in the dictionary.

# dict.values(): Returns a view object with all the values in the dictionary.

# dict.update(other_dict): Updates the dictionary with key-value pairs from another dictionary.

# Iterating Over Dictionaries

# You can iterate over a dictionary using a for loop to access keys, values, or both:

for key in my_dict:
    print(key, my_dict[key]) # Prints each key and its associated value

# Nested Dictionaries

# Dictionaries can contain other dictionaries, allowing you to create nested data structures:

nested_dict = {
    "child1": {
        "name": "Emily",
        "age": 5
    },
    "child2": {
        "name": "John",
        "age": 4
    }
}

# To access values in a nested dictionary, you chain the keys together:

print(nested_dict["child1"]["name"]) # Output: Emily
