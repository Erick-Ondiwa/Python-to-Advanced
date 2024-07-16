# This program describes how to move files from one location to another
# 1. Import the os and os path
import os

import os.path
source = "trial.txt"  # this is the source of the file
destination = "C:\\Users\\Erick Ondiwa'z\\Desktop\\trial.txt" # this is the target destination

try:
    if os.path.exists(destination):  # we try if the destination alrady exists, then we pose an error
        print("The destination contains a file with the same name")
    else:
        os.replace(source, destination)  # else we move the file using the .replace method
except FileNotFoundError:
    print(source+" not found")  # we handle the error if the source isn't found
else:
    print(source+" was transferred to "+destination)
