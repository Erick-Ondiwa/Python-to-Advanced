# Printing 'hello world' in Python

from datetime import date
from datetime import datetime
names = ["Erick Ondiwa", "James Wasonga", "Felix Awere", "Shadrack Mutinda", "Mark Emmanuel"]

year_of_births = [2000, 2001, 2002, 2003, 2004]

name_idx = 0
# current_year = date.today()

for name in names:
    person_year = year_of_births[name_idx]
    current_year = datetime.now().year

    age = current_year - person_year
    # yob_idx = 0
    print(f"{name} you are:{age} years old.")

    name_idx += 1





