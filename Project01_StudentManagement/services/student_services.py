from models.student import Student

students = []


def add_student(name, age, roll, marks):
    students.append(Student(name, age, roll, marks))


def display_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        student.display()


def search_student(roll):
    for student in students:
        if student.get_roll() == roll:
            student.display()
            return student

    print("Student not found.")
    return None


def update_student(roll, name, age, marks):
    student = search_student(roll)

    if student:
        student.set_name(name)
        student.set_age(age)
        student.set_marks(marks)
        print("Student Updated Successfully")


def delete_student(roll):
    global students

    for student in students:
        if student.get_roll() == roll:
            students.remove(student)
            print("Student Deleted Successfully")
            return

    print("Student not found.")


def average_marks():
    if not students:
        return 0

    total = sum(student.get_marks() for student in students)

    return total / len(students)


def topper():
    if not students:
        return None

    return max(students, key=lambda student: student.get_marks())