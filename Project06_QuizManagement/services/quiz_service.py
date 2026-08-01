from models.quiz import Quiz

questions = []
score = 0


def load_questions(question_list):
    global questions
    questions = question_list


def conduct_quiz():
    global score

    if not questions:
        print("No Questions Available")
        return

    score = 0

    for question in questions:

        question.display()

        try:
            answer = int(input("Enter your answer (1-4): "))

            if answer == question.get_answer():
                score += 1

        except ValueError:
            print("Invalid Input")

    print(f"\nFinal Score: {score}/{len(questions)}")


def get_score():
    return score