import random


def play_game():
    user_choice = None
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    while user_choice not in choices:
        user_choice = input("What's your choice,Rock, Paper or Scissors?: ").lower()

        result = " "
        if user_choice == computer:
            result = "You Tie!"
        elif user_choice == "rock" and computer == "paper":  # 1
            result = "You Lose!"
        elif user_choice == "rock" and computer == "scissors":  # 2
            result = "You Win!"
        elif user_choice == "paper" and computer == "rock":  # 3
            result = "You Win!"
        elif user_choice == "paper" and computer == "scissors":  # 4
            result = "You Lose!"
        elif user_choice == "scissors" and computer == "Rock":  # 5
            result = "You Win!"
        elif user_choice == "scissors" and computer == "paper":
            result = "You Lose!"
        print("You: " + user_choice + ", " + "Computer:" + computer)
        return result


class Scores:
    wins = 0
    losses = 0
    ties = 0
    attempts = 0


def display_result():
    while Scores.attempts <= 2:
        Scores.attempts += 1
        result = play_game()
        print(result)

        if result == "You Win!":
            Scores.wins += 1
        elif result == "You Lose!":
            Scores.losses += 1
        elif result == "You Tie!":
            Scores.ties += 1
        else:
            print("This is an invalid result")
        print("Wins: " + str(Scores.wins) + " Losses " + str(Scores.losses) + " Ties " + str(
            Scores.ties))
    print("You've reached a maximum of " + str(Scores.attempts) + " attempts")
    play_again()

    return Scores


display_result()


def play_again():
    user_response = input("Play again? yes/no: ").upper()
    while True:
        if user_response == "NO":
            print("Goodbyeee")
            break
        else:
            display_result()
# while play_again():
#     display_result()


# while display_result():
#     play_again()
# print("Goodbyeeee!")
