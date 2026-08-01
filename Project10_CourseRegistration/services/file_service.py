import csv
from models.student import Student


def save_students(students):

    with open("data/registrations.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Courses"]
        )

        for student in students:

            writer.writerow([
                student.get_id(),
                student.get_name(),
                ",".join(student.get_courses())
            ])

    print("Records Saved Successfully")


def load_students():

    students = []

    try:

        with open("data/registrations.csv", "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                return students

            for row in rows[1:]:

                student = Student(
                    int(row[0]),
                    row[1]
                )

                if row[2]:
                    for course in row[2].split(","):
                        student.add_course(course)

                students.append(student)

    except FileNotFoundError:

        pass

    return students