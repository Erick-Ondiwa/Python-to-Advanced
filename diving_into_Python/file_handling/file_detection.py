# Importing the os module which contains the path submodule
import os
import os.path
file_path = "trial.txt"
print(file_path)

# The .exists() method returns true if the specified file path exists
if os.path.exists(file_path):
    print("The location exists")
    # The .isfile() method returns true if the specified file is a file otherwise it returns false
    if os.path.isfile(file_path):
        print("This is a file")

        # The .isdir() method returns true if the specified file is a directory otherwise it returns false
    elif os.path.isdir(file_path):
        print("It is a directory")
else:
    print("The location doesn't exist")
