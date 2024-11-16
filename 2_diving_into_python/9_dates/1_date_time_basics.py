# In Python, handling dates and times is done primarily with the datetime module, which provides
# classes for date and time manipulation. This module can be used to create, manipulate, format,
# and retrieve date and time values easily.

# 1. Basic Date and Time Handling
# You can use datetime.datetime to create date and time objects in Python.

import datetime
# import pygame
# from datetime import datetime

# To get Today's date:
today = datetime.date(2025, 1, 2).today()
print(today)

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# When you want to set time to a specific time
set_time = datetime.time(12, 40, 20)

current_time = datetime.datetime.now().strftime('%H:%M:%S')
print(f"The time is: {current_time}")


# ##### CHECK THE pygame module
# Creating an alarm clock
# For sound effects in an alarm, import the pygame module
