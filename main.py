# #  program to compute the area volume of a cylinder
#
# # A function to compute the cross-section area of a circle
# def compute_circle_area(radius):
#     pi = 3.142
#
#     return pi * radius * radius
#
#
# def compute_volume():
#     height = 40
#     area = compute_circle_area(14)
#     return area * height
#
#
# volume = compute_volume()
# print(volume)
#
#
# def compute_sum(*numbers):
#     total = 0
#     for nums in numbers:
#         total += nums
#     print(total)
#
#
# compute_sum(10, 20, 30, 40, 50)
#
#
# def sayHi(**fullname):
#     print("Dear", end=" ")
#     for key, value in fullname.items():
#         print(value, end=" ")
#     print(",")
#
#
# sayHi(tittle="Eng.", first_name="Erick", middle_name="Ochieng", last_name="Ondiwa")

import os

file_path = "C:\\Users\\Erick Ondiwa'z\\Desktop\\trial.txt"
 
# Checking if the file exists
if os.path.exists(file_path):
    print("The specified file exists")
else:
    print("Could not trace the specified file path")
