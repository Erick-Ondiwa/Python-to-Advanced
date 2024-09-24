# The split() method in Python is a powerful string manipulation tool used to divide a string into
# a list of substrings based on a specified delimiter. By default, if no delimiter is provided,
# it splits the string based on whitespace (spaces, tabs, or newlines).

# This method divides a string into an ordered list of substrings, places these
# substrings into a list, and returns the list. The division is done by searching for a
# specified pattern; the default is to split on any whitespace.

# Syntax:
delimiter = " "
max_split = " "
str.split(delimiter, max_split)
# Parameters:
# delimiter/separator (optional): The delimiter string on which the split operation is performed.
# If omitted, any whitespace is treated as the separator.

# max_split (optional): The number of splits you want to perform. If not provided or set to -1,
# there is no limit, and all possible splits are made.
# Return Value:

# The split() method returns a list of substrings.

# Example 1: Basic Usage (Default Behavior)
text = "Python is an amazing language"
result = text.split()
print(result)

# Output:
output1 = ['Python', 'is', 'an', 'amazing', 'language']

# Here, split() divides the string into a list of words based on spaces.

# Example 2: Specifying a Separator

text = "apple,banana,cherry,grape"
result = text.split(",")
print(result)
# Output:
output2 = ['apple', 'banana', 'cherry', 'grape']
# In this case, the string is split by commas.

# Example 3: Using the max_split Parameter

text = "Python is easy to learn"
result = text.split(" ", 2)  # Split at the first two spaces
print(result)

# Output:
output3 = ['Python', 'is', 'easy to learn']
# Here, the string is split only twice (at the first two spaces), and the remainder of the string
# is kept intact.

# Example 4: Splitting by Multiple Spaces
# The split() method can handle multiple spaces between words without any additional steps.

text = "Python   is   fun"
result = text.split()  # Default is splitting by whitespace
print(result)
# Output:
output4 = ['Python', 'is', 'fun']
# Notice how it ignores the multiple spaces and only splits at meaningful intervals.

# Example 5: Using Non-Whitespace Separator

text = "2024-09-24"
result = text.split("-")
print(result)

# Output:
output5 = ['2024', '09', '24']

date_of_birth = "2001-10-07-12:00noon"
new_dob = date_of_birth.split("-", -1)[:3]

print(new_dob)
# This example demonstrates splitting a date string based on the - separator.

# Example 6: Using split() with No Splitting
# If the separator doesn't exist in the string, the entire string is returned as a single element
# in the list:

text = "HelloWorld"
result = text.split(",")
print(result)

# Output:
output6 = ['HelloWorld']

# Important Points to Remember:
# If you pass an empty string "" as the separator, a ValueError will be raised.
# The split() method only operates on string objects. To apply it to other data types, you need to
# convert them to strings first.

# Example 7: Splitting a String with No Separator (Raises Error)

text = "HelloWorld"
# text.split("")  # This would raise a ValueError

# Practical Use Cases:
# Parsing CSV data: You can split CSV strings (comma-separated values) into lists.
# Tokenizing text: Useful in natural language processing (NLP) to break down sentences into words
# or tokens.
# Date and time formatting: You can split dates and times to extract specific parts like the day,
# month, or year.

