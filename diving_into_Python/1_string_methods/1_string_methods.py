# There are several built in string methods available in python. They include:
first_name = "erick"
middle_name = "Ochieng"
last_name = "Ondiwa"

full_name = first_name.capitalize() + "@" + middle_name + "@" + last_name
print(full_name)
# len(): This method returns the length or the number of chars in a specified string
# capitalize(): This method capitalizes the first letter of every word in the string
print(first_name.capitalize())

# upper():This method changes all the letters in a string to uppercase
print(first_name.upper())

# lower(): This method changes all the letters in a string to lowercase
print(last_name.lower())
# find(): This method returns the index of first occurrence of a specified letter or substring
# within a string
# rfind(): This method returns the index of last occurrence of a specified letter or substring
# within a string
print(full_name.find(" "))

# replace(): This method replaces a character with another character or a string with another
# string. This method takes three arguments, old char or string, new char or string, the number
# of instances or occurrences  of the old
# string to be replaced with the new string
new_name = full_name.replace("@", " ", 2)
print(new_name)

# count(): This method returns the number of occurrences of a specified char or substring in a
# string of text

print(new_name.count("i"))

# title(): Changes a string or a specified portion of a string to title case
print(new_name.title())

letter = "eRiCk"
print(letter.swapcase())

# center(): This method pads the string with the specified character

# swapcase(): This method swaps the cases of all characters in a string
print(new_name.swapcase())
# casefold(): Implements the caseless string matching. This method is similar to the  lower
# method but stronger as it is thorough in handling special cases and characters from
# different languages

print(new_name.casefold())

# center():
# strip()
# isdigit(): # Returns True if a variable is a digit, else false
# isalpha(): Returns True if a variable contains only alphabetical chars excluding space,
# else false
# isalnum():


