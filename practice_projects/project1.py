import random


def computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)


def compute_user_choice():
    return input("What's your choice,Rock, Paper or Scissors? ")


def compute_result(user, computer):
    result = " "
    if user == computer:
        result = "You Tie!"

    elif user == "Rock" and computer == "Paper":                    # 1
        result = "You Lose!"

    elif user == "Rock" and computer == "Scissors":                # 2
        result = "You Win!"

    elif user == "Paper" and computer == "Rock":             # 3
        result = "You Win!"

    elif user == "Paper" and computer == "Scissors":             # 4
        result = "You Lose!"

    elif user == "Scissors" and computer == "Rock":             # 5
        result = "You Win!"

    elif user == "Scissors" and computer == "Paper":
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
    print("Wins: "+str(wins)+" Losses "+str(losses)+" Ties "+str(ties))


display_result()
