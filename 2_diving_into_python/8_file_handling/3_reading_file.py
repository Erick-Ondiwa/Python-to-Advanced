import os

import os.path

try:
    with open("trial.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Could not access the specified file name")
except NameError:
    print("Could not access the specified file name")
else:
    print(content)


# Reading a .json File
import json
try:
    with open("trial.json", "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("Could not access the specified file name")
except NameError:
    print("Could not access the specified file name")
else:
    print(content)


# Reading a csv File
import csv
try:
    with open("trial.csv", "r") as file:
        content = csv.reader(file)
        for line in content:  # Data from a csv is read line by line hence looping
            print(line)
except FileNotFoundError:
    print("Could not access the specified file name")
except NameError:
    print("Could not access the specified file name")
else:
    print(content)

