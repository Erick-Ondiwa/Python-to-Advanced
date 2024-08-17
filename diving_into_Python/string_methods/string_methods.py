# There are several built in string methods available in python. They include:
first_name = "erick"
middle_name = "Ochieng"
last_name = "Ondiwa"

full_name = first_name.capitalize() + "@" + middle_name + "@" + last_name
print(full_name)
# capitalize(): This method capitalizes the first letter of every word in the string
print(first_name.capitalize())

# upper():This method changes all the letters in a string to uppercase
print(first_name.upper())

# lower(): This method changes all the letters in a string to lowercase
print(last_name.lower())
# find(): This method returns the index of a specified letter or substring within a string
print(full_name.find(" "))

# replace(): This method replaces a character with another character or a string with another
# string. This method takes three arguments, old char or string, new char or string, the number
# of instances or occurrences  of the old
# string to be replaced with the new string
new_name = full_name.replace("@", " ", 2)
print(new_name)

# title(): Changes a string or a specified portion of a string to title case
print(new_name.title())

letter = "eRiCk"
print(letter.swapcase())

# swapcase(): This method swaps the cases of all characters in a string
print(new_name.swapcase())
# casefold(): Implements the caseless string matching
# isdigit():
# isalpha():
# isalphanum
