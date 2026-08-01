import csv
from models.student import Student


def save_students(students):
    with open("data/students.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Roll", "Name", "Age", "Marks"])

        for student in students:
            writer.writerow([
                student.get_roll(),
                student.get_name(),
                student.get_age(),
                student.get_marks()
            ])


def load_students():
    students = []

    try:
        with open("data/students.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                students.append(
                    Student(
                        row[1],
                        int(row[2]),
                        int(row[0]),
                        float(row[3])
                    )
                )

    except FileNotFoundError:
        pass

    return students