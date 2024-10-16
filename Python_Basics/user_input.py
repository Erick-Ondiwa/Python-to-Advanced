# Accepting User Input with type hinting
# The input() Method

length: float = float(input("Enter length:"))
width: float = float(input("Enter width:"))
area: float = length * width
print("Area = " + str(area) + "cm2")

# String Slicing - this a way of creating a substring from a portion of another string
full_name: str = "Erick Ondiwaz"
first_name: str = full_name[slice(0, 6)]
last_name: str = full_name[slice(6, 13)]

print("Your name is "+first_name + last_name)
website_url: str = "https://google.com"
site_name: str = website_url[slice(8, -4)]
print(site_name)
