import random


def play_game():
    user_choice = None
    choices = ("rock", "paper", "scissors")
    computer = random.choice(choices)
    while user_choice not in choices:
        user_choice = input("What's your choice,Rock, Paper or Scissors?: ").lower()
        if user_choice == computer:
            return "You Tie!"
        elif ((user_choice == "rock" and computer == "paper" or
              user_choice == "paper" and computer == "scissors") or
              user_choice == "scissors" and computer == "paper"):  # 1
            return "You Lose!"

        elif ((user_choice == "rock" and computer == "scissors" or
              user_choice == "paper" and computer == "rock") or
              user_choice == "scissors" and computer == "Rock"):  # 2
            return "You Win!"

        print("You: " + user_choice + ", " + "Computer:" + computer)


class Scores:
    wins = 0
    losses = 0
    ties = 0
    attempts = 0


def display_result():
    while Scores.attempts <= 2:
        Scores.attempts += 1
        print()
        print(f"**********ATTEMPT NO:{Scores.attempts}************")
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
