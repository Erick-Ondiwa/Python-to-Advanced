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

for key, value in my_dict.items():
    print(key, value)

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

#            1. dict.get(key, default)
# Returns the value associated with key if it exists in the dictionary; otherwise, it returns the
# default value (which is None if not specified). This method avoids KeyError if the key does not
# exist.

person = {'name': 'Alice', 'age': 25}
print(person.get('name'))           # Output: Alice
print(person.get('address', 'N/A'))  # Output: N/A

#           2. dict.keys()
# Returns a view object that displays all the keys in the dictionary. The view object can be
# converted to a list if needed.

person = {'name': 'Alice', 'age': 25}
print(person.keys())               # Output: dict_keys(['name', 'age'])
print(list(person.keys()))         # Output: ['name', 'age']

#           3. dict.values()
# Returns a view object that displays all the values in the dictionary.

person = {'name': 'Alice', 'age': 25}
print(person.values())             # Output: dict_values(['Alice', 25])
print(list(person.values()))       # Output: ['Alice', 25]

#           4. dict.items()
# Returns a view object that displays each key-value pair as a tuple within a list-like view object.

person = {'name': 'Alice', 'age': 25}
print(person.items())              # Output: dict_items([('name', 'Alice'), ('age', 25)])

#           5. dict.pop(key, default)
# Removes the specified key and returns its associated value. If the key is not found, it returns
# the default value if provided; otherwise, it raises a KeyError.

person = {'name': 'Alice', 'age': 25}
age = person.pop('age')
print(age)                         # Output: 25
print(person)                      # Output: {'name': 'Alice'}

#           6. dict.popitem()
# Removes and returns the last inserted key-value pair as a tuple. This method raises a KeyError
# if the dictionary is empty.

person = {'name': 'Alice', 'age': 25}
last_item = person.popitem()
print(last_item)                   # Output: ('age', 25)
print(person)                      # Output: {'name': 'Alice'}

#           7. dict.update([other])
# Updates the dictionary with the key-value pairs from another dictionary or an iterable of
# key-value pairs. If a key exists, its value will be updated; if not, the key-value pair wil  be
# added.

person = {'name': 'Alice', 'age': 25}
person.update({'age': 26, 'city': 'New York'})
print(person)                      # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

#           8. dict.clear()
# Removes all items from the dictionary, making it empty.

person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)                      # Output: {}

#           9. dict.copy()
# Returns a shallow copy of the dictionary. This is useful when you want to make a copy without
# modifying the original dictionary.

person = {'name': 'Alice', 'age': 25}
person_copy = person.copy()
person_copy['age'] = 30
print(person)                      # Output: {'name': 'Alice', 'age': 25}
print(person_copy)                 # Output: {'name': 'Alice', 'age': 30}

#           10. dict.fromkeys(keys, value)
# Creates a new dictionary with the specified keys and sets all values to value (default is
# None). This is a class method that does not modify the original dictionary.

keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys, 'N/A')
print(new_dict)                    # Output: {'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}

#           11. setdefault(key, default)
# If the key exists, it returns the value associated with key. If the key does not exist,
# it adds key with the default value and returns default.The default value is None if not specified.

person = {'name': 'Alice'}
age = person.setdefault('age', 25)
print(age)                         # Output: 25
print(person)                      # Output: {'name': 'Alice', 'age': 25}

# ####### Practical Example: Using Dictionary Methods

inventory = {'apple': 10, 'banana': 5, 'orange': 7}

# Adding items to the inventory
inventory.update({'mango': 3, 'pear': 4})

# Removing an item
inventory.pop('banana')

# Checking for a specific item
if 'apple' in inventory:
    print(f"Apples available: {inventory.get('apple')}")

# Display all items
for fruit, quantity in inventory.items():
    print(f"{fruit}: {quantity}")

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
