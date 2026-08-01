from models.student import Student

students = []


def add_student(student_id, name):

    students.append(Student(student_id, name))

    print("Student Added Successfully")


def search_student(student_id):

    for student in students:

        if student.get_id() == student_id:
            return student

    return None


def display_students():

    if not students:
        print("No Students Found")
        return

    for student in students:
        student.display()


def register_course(student_id, course):

    student = search_student(student_id)

    if student:

        student.add_course(course)

        print("Course Registered Successfully")

    else:

        print("Student Not Found")


def drop_course(student_id, course):

    student = search_student(student_id)

    if student:

        student.drop_course(course)

        print("Course Dropped Successfully")

    else:

        print("Student Not Found")


def delete_student(student_id):

    global students

    for student in students:

        if student.get_id() == student_id:

            students.remove(student)

            print("Student Deleted Successfully")

            return

    print("Student Not Found")