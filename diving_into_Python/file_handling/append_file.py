import os
try:
    with open("trial.txt", "a") as file:
        appended_text = file.write(
            "I'm currently learning python.\n This is as a result of being passionate about data "
            "science.")
except Exception:
    print("Could not find the specified file.")
else:
    print("Data has been added successfully")