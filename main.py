# #  program to compute the area volume of a cylinder
#
# # A function to compute the cross-section area of a circle
# def compute_circle_area(radius):
#     pi = 3.142
#
#     return pi * radius * radius
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
#
# import os
#
# file_path = "C:\\Users\\Erick Ondiwa'z\\Desktop\\trial.txt"
#
# # Checking if the file exists
# if os.path.exists(file_path):
#     print("The specified file exists")
# else:
#     print("Could not trace the specified file path")
# import random
#
#
# def computer_choice():
#     choices = ["Rock", "Paper", "Scissors"]
#     return random.choice(choices)
#
#
# def compute_user_choice():
#     return input("What's your choice,Rock, Paper or Scissors? ")
#
#
# def compute_result(user, computer):
#     result = " "
#     if user == computer:
#         result = "You Tie!"
#
#     elif user == "Rock" and computer == "Paper":                    # 1
#         result = "You Lose!"
#
#     elif user == "Rock" and computer == "Scissors":                # 2
#         result = "You Win!"
#
#     elif user == "Paper" and computer == "Rock":             # 3
#         result = "You Win!"
#
#     elif user == "Paper" and computer == "Scissors":             # 4
#         result = "You Lose!"
#
#     elif user == "Scissors" and computer == "Rock":             # 5
#         result = "You Win!"
#
#     elif user == "Scissors" and computer == "Paper":
#         result = "You Lose!"
#
#     print("You: " + user + ", " + "Computer:" + computer)
#     return result
#
#
# def display_result():
#     wins = 0
#     losses = 0
#     ties = 0
#
#     comp_choice = computer_choice()
#     user_choice = compute_user_choice()
#     result = compute_result(comp_choice, user_choice)
#     print(result)
#     if result == "You Win!":
#         wins += 1
#     elif result == "You Lose!":
#         losses += 1
#     elif result == "You Tie!":
#         ties += 1
#     else:
#         print("This is an invalid result")
#     print("Wins: "+str(wins)+" Losses "+str(losses)+" Ties "+str(ties))
#
#
# display_result()
#
#
# def compute_attempts():
#     attempts = 0
#     display_result()
#     while display_result():
#         attempts += 1
#     print(attempts)

class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        return f"I'm a {self.name}. I'm {self.age} years old."


class Child(Animals):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.name = name


animal1 = Child("Dog", 24, "kidding")
print(animal1.sayHi())




