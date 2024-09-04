# ####### THIS IS A QUIZ APP ########
questions = ["Which is the largest planet?",
             "How long does it take the sun to revolve around the sun?",
             "Which is the most abundant substance on the earth surface?",
             "Which is the cheapest mode of transport?",
             "I am an unlucky number. Who am I?"]
guesses = []
questions_idx = 0
answers = ("A", "B", "C", "D", "D")
options = [["A. Mercury ", "B. Mars ", "C. Jupiter ", "D. Earth "],
           ["A. 288 ", "B. 365 ", "C. 400 ", "D. 364 "],
           ["A. Air ", "B. Water ", "C. Soil ", "D. Plants "],
           ["A. Road ", "B. Air ", "C. Water ", "D. Pipeline "],
           ["A. 7 ", "B. 15 ", "C. 13 ", "D. 17 "]]

correct_choices = 0

for question in questions:
    print(question)
    for option in options[questions_idx]:
        print(option)

    choices = ("A", "B", "C", "D")
    user_choice = input("Please select: A, B, C or D: ").upper()
    while user_choice not in choices:
        user_choice = input("Please select: A, B, C or D: ").upper()
    guesses.append(user_choice)

    if user_choice == answers[questions_idx]:
        print("CORRECT")
        correct_choices += 1
    else:
        print("INCORRECT")
    print("*********************************************************")
    print()
    questions_idx += 1

score = (correct_choices / len(answers)) * 100
print(f"Your score is:{score}%")
