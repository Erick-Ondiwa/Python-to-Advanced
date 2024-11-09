# Accepting User Input with type hinting
# The input() Method

# Practice 1
name = input("What is your name? ")
age = int(input("How old are you? "))
age = age + 1
print(f"Hello {name}")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

# Practice 2
length: float = float(input("Enter length:"))
width: float = float(input("Enter width:"))
area: float = length * width
print(f"Area = {area}cm2")


# Exercise: Shopping Cart Program
item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many items would you like to buy? "))

total = price * quantity

print(f"You bought {quantity} {item}. Your total is {total}")


# String Slicing - this a way of creating a substring from a portion of another string
full_name: str = "Erick Ondiwaz"
first_name: str = full_name[slice(0, 6)]
last_name: str = full_name[slice(6, 13)]

# print("Your name is "+first_name + last_name)
website_url: str = "https://google.com"
site_name: str = website_url[slice(8, -4)]
# print(site_name)
