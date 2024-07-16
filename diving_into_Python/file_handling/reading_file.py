import os

import os.path

try:
    with open("trial.txt", "r") as file:
        read_file = file.read()
except FileNotFoundError:
    print("Could not access the specified file name")
except NameError:
    print("Could not access the specified file name")
else:
    print(read_file)