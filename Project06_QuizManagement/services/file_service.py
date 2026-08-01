import csv
from models.quiz import Quiz


def load_questions_from_file():

    questions = []

    try:

        with open("data/questions.csv", "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                return questions

            for row in rows[1:]:

                questions.append(

                    Quiz(

                        row[0],

                        [row[1], row[2], row[3], row[4]],

                        int(row[5])

                    )

                )

    except FileNotFoundError:

        print("questions.csv not found.")

    return questions


def save_result(score, total):

    with open("data/results.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([score, total])

    print("Result Saved Successfully")