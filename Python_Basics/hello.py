# Printing 'hello world' in Python

print("Hello World")

name = "Erick Ondiwaz"
print("Hello "+name)

names = ["Erick Ondiwa", "James Wasonga", "Felix Awere", "Shadrack Mutinda", "Mark Emmanuel"]

year_of_births = [2000, 2001, 2002, 2003, 2004]

# for year_of_birth in year_of_births:
#     print(year_of_birth)

name_idx = 0

for name in names:
    years = year_of_births[name_idx]
    print(f"{name}:{years}")

    name_idx += 1



