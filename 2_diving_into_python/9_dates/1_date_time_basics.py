# In Python, handling dates and times is done primarily with the datetime module, which provides
# classes for date and time manipulation. This module can be used to create, manipulate, format,
# and retrieve date and time values easily.

# 1. Basic Date and Time Handling
# You can use datetime.datetime to create date and time objects in Python.

import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# To get Today's date:
today = datetime.date(2025, 1, 2).today()
print(today)

current_time = datetime.datetime.now().strftime('%H:%M:%S- %D')
print(current_time)
