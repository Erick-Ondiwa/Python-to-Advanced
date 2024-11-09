# this section describes how to delete files, empty folders and folders containing files
# In order to delete a file we need to import the os

# Deleting a file
import os

file_path = "copy.txt"
try:
    os.remove(file_path)
except FileNotFoundError:
    print("The specified file doesn't exist")
else:
    print("The file has been deleted successfully")

# Deleting an empty folder

folder_path = "copy.txt"
try:
    os.rmdir(folder_path)

except FileNotFoundError:
    print("The specified file doesn't exist")

except NotADirectoryError:
    print("The specified file path isn't a directory")
else:
    print("The file has been deleted successfully")

# # Deleting a folder containing files
import shutil

folder_name = "practice_folder"
try:
    shutil.rmtree(folder_name)
except:
    print(" ")
