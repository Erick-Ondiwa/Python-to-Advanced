# String slicing is a method of creating a substring from a portion of another string.
# There are two ways of slicing a string:
# 1. The indexing operator []: This works in a similar manner as indexes in lists

full_name = "Maseno University"
first_name = full_name[0:7]
last_name = full_name[7:]
short_name = full_name[:10:4]
print(last_name)
print(first_name)
print(short_name)

# 2. The slice() function: This object also takes the same number of arguments as the indexing
# operator
website_url = "http://www/erickondiwa.com"
username = website_url[slice(11, -4)]
print(username)
