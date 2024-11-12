import json
import os

# import os.path
from os import path as filepath

crafters = ["Erick Ondiwa", "Shadrack Mutinda", "Kelvin Gichohi", "Mark Emmanuel"]

# try:
#     print("The file was found")
#     # the open() method takes two parameters, the filepath, the mode
#
#     with open("trial.txt", "w") as file:  # w => Opens a file for writing. If the file already
#         # exists, it overwrites the file, effectively clearing its contents. If the file does not
#         # exist, it creates a new file.
#
#         # x => Opens a file for writing only if it does not already exist. If the file already
#         # exists, this mode raises a FileExistsError, preventing accidental overwriting
#
#         for crafter in crafters:  # A list object can't be written directly to a file
#             written_data = file.write(f"{crafter}\n")
#
# except FileNotFoundError:
#     print("Could not access the specified file name")
# except NameError:
#     print("Could not access the specified file name")

# student_details = {"name": "Erick Ondiwa", "age": 21, "course": "Computer science"}
#
# # Writing to a .json File
# import json
#
# file_path = "C:/Users/ErickOndiwa/Desktop/json_data.json"
# with open(file=file_path, mode="w") as stu_file:
#     # the json.dump function accepts upto 3 parameters;
#     json.dump(student_details, stu_file, indent=4)
#     print(f"The .json file was created")

# Writing to a .csv File
import csv
csv_data = [["Name", "Age", "Job Position"],
            ["Erick", 21, 'Computer Science'],
            ["Victor", 22, "Electrical Engineering"],
            ["Newton", 22, "Nursing"],
            ["Luke", 22, "Software Engineering"]]

file_path = "C:/Users/ErickOndiwa/Desktop/csv_data.csv"
with open(file=file_path, mode="w", newline="") as csv_file:
    # writer = csv.writer(csv_file)
    for row in csv_data:
        csv.writer(csv_file).writerow(row)
    print(f"The .csv file was created")
