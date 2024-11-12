# To copy the contents of one file into another, you need to import the shutil module.
import shutil
# This module contains three methods:
# 1. copyfile - simply copies the contents of one file into another file
# 2. copy
# - this copies the contents of a file plus permission mode and the destination can either be a
# file or a directory
# 3. copy2 - this includes the contents in copy plus the file creation and modification times (
# File's metadata)
#
shutil.copy("trial.txt", "copy.txt")