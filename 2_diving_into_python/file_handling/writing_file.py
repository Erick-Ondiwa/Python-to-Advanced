import json
import os

# import os.path
from os import path as filepath

crafters = ["Erick Ondiwa", "Shadrack Mutinda", "Kelvin Gichohi", "Mark Emmanuel"]

try:
    print("The file was found")
    # the open() method takes two parameters, the filepath, the mode
    with open("trial.txt", "w") as file:  # w => writing to an already existing file. x =>
        # writing to a new file
        for crafter in crafters:
            written_data = file.write(f"{crafter}\n")

except FileNotFoundError:
    print("Could not access the specified file name")
except NameError:
    print("Could not access the specified file name")

student_details = {"name": "Erick Ondiwa", "age": 21, "course": "Computer science"}

file_path = "C:/Users/ErickOndiwa/Desktop/json_data.txt"
with open(file=file_path, mode="w") as stu_file:
    # the json.dump function accepts 3 parameters;
    json.dump(student_details, stu_file, indent=4)
    print(f"The file {file_path} was created")
