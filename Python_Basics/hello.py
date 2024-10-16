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
    # print(f"{name} you are:{age} years old.")

    name_idx += 1


student_heights = [180, 124, 165, 173, 189, 169, 146]

heights_idx = 0
sum_height = 0

for student_height in student_heights:
    sum_height += student_heights[heights_idx]

    heights_idx += 1

average_sum = sum_height / len(student_heights)
average_sum = round(average_sum, 2)

print(f"The sum total of heights is: {sum_height}.")
print(f"The average height for all the students is:{average_sum}.")


sum_nums = 0
for nums in range(1, 101):
    if nums % 2 == 0:
        sum_nums += nums
print(sum_nums)


ages = []

person_idx = 0
while len(ages) < 4:
    person_idx += 1
    user_ages = int(input(f"Please enter person {person_idx} age:"))
    ages.append(user_ages)


sum_ages = 0
average_age = 0
for age in ages:
    sum_ages += age
average_age = sum_ages / len(ages)
average_age = round(average_age, 2)

print(f"The average age for the {person_idx} people is: {average_age}")

nums = [1, 1, 2, 2, 5, 5, 5, 6, 7, 7, 3]
for num in nums:
    count_of_num = num
