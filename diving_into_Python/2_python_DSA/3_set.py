# Understanding Python Sets

# Sets in Python are a collection data type that is unordered, unchangeable, and indexed. They are
# similar to lists or dictionaries but with a key difference that they only contain unique
# elements and do not support duplicates. This makes sets particularly useful for membership
# testing, removing duplicates from a sequence, and performing mathematical operations like
# unions, intersections, and set differences.

# Creating and Initializing Sets

# Sets can be created using the set() constructor or by using curly braces {}. Here's an example
# of creating a set with the set() constructor:

fruits = set(["apple", "banana", "cherry"])
print(fruits)

# Alternatively, you can create a set with curly braces:

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Note that sets are unordered, so the items have no index and can appear in a different order
# every time you use them. Also, sets do not allow mutable items like lists or dictionaries to be
# included.

# Basic Set Operations

# Python provides a variety of operations that can be performed on sets. These include:

# Union (| or union() method): Combines two sets and returns a new set containing all unique
# elements.

# Intersection (& or intersection() method): Returns a new set with elements that are common to
# all sets.

# Difference (- or difference() method): Returns a new set with elements in the first set that are
# not in the others.

# Symmetric Difference (^ or symmetric_difference() method): Returns a new set with elements in
# either the first or second set, but not both.

# Here's an example of set operations:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# Union
print(set1 | set2)

# Intersection
print(set1 & set2)

# Difference
print(set1 - set2)

# Symmetric Difference
print(set1 ^ set2)

# Modifying Sets

# Sets are mutable, meaning you can add or remove items after a set has been created. Some methods
# to modify sets include:

# add(): Adds a single element to the set.

# update(): Adds multiple elements to the set.

# remove(): Removes a specific element from the set.

# discard(): Removes a specific element from the set without raising an error if the element is
# not found.

# pop(): Removes and returns an arbitrary set element.

# clear(): Removes all elements from the set.

# Here's an example of modifying a set:

# Initialize a set
numbers = {1, 2, 3}

# Add an element
numbers.add(4)

# Remove an element
numbers.remove(2)

# Discard an element
numbers.discard(5) # No error if the element is not found

# Pop an element
print(numbers.pop())

# Clear the set
numbers.clear()

# Frozen Sets

# Python also provides the frozenset type, which is like a set but immutable. Once created,
# items cannot be added or removed from a frozenset. This is useful when you need to create a set
# that you don't want to change over time.

immutable_fruits = frozenset(["apple", "banana", "cherry"])

# When to Use Sets

# Sets are a good choice when you need to maintain a collection of unique items, perform set
# operations like those in mathematics, or when you need to efficiently check for the presence of
# an element. However, since sets are unordered, they are not suitable when the order of elements
# is important.
