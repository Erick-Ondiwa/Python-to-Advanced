import random

# while True:

choices = ["rock", "paper", "scissors"]


def computer_choice():
    return random.choice(choices)


def compute_user_choice():
    user_choice = input("What's your choice,Rock, Paper or Scissors?: ").lower()
    if user_choice in choices:
        return user_choice
    else:
        print("Invalid choice please ensure you type in either rock, paper or scissors!")


def compute_result(user, computer):
    result = " "
    if user == computer:
        result = "You Tie!"
    elif user == "rock" and computer == "paper":  # 1
        result = "You Lose!"
    elif user == "rock" and computer == "scissors":  # 2
        result = "You Win!"
    elif user == "paper" and computer == "rock":  # 3
        result = "You Win!"
    elif user == "paper" and computer == "scissors":  # 4
        result = "You Lose!"
    elif user == "scissors" and computer == "Rock":  # 5
        result = "You Win!"
    elif user == "scissors" and computer == "paper":
        result = "You Lose!"
    print("You: " + user + ", " + "Computer:" + computer)
    return result


def display_result():
    wins = 0
    losses = 0
    ties = 0

    comp_choice = computer_choice()
    user_choice = compute_user_choice()
    result = compute_result(comp_choice, user_choice)
    print(result)
    if result == "You Win!":
        wins += 1
    elif result == "You Lose!":
        losses += 1
    elif result == "You Tie!":
        ties += 1
    else:
        print("This is an invalid result")
    print("Wins: " + str(wins) + " Losses " + str(losses) + " Ties " + str(ties))


display_result()
#
#     user_response = input("Play again? Yes/No: ").lower()
#     if user_response != "yes":
#         break
#     else:
#
# print("Goodbyeeee!")
