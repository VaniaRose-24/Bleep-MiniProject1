from services.quiz_service import *
from services.file_service import *

questions = load_questions_from_file()

load_questions(questions)

while True:

    print("""
========== QUIZ MANAGEMENT SYSTEM ==========

1. Start Quiz
2. Save Result
3. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        conduct_quiz()

    elif choice == "2":

        save_result(get_score(), len(questions))

    elif choice == "3":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")