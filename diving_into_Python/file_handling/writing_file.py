import os

import os.path

# try:
with open("trial.txt", "w") as file:
    written_data = file.write("My name is Erick Ondiwaz.\n I am the code crafter.")

# except FileNotFoundError:
#     print("Could not access the specified file name")
# # except NameError:
# #     print("Could not access the specified file name")
# else:
#     print(written_data)