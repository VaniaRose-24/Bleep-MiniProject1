from services.registration_service import *
from services.file_service import *

from services.registration_service import students

students.extend(load_students())

while True:

    print("""
========= COURSE REGISTRATION SYSTEM =========

1. Add Student
2. Display Students
3. Register Course
4. Drop Course
5. Delete Student
6. Save Records
7. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        student_id = int(input("Student ID : "))
        name = input("Student Name : ")

        add_student(student_id, name)

    elif choice == "2":

        display_students()

    elif choice == "3":

        student_id = int(input("Student ID : "))
        course = input("Course Name : ")

        register_course(student_id, course)

    elif choice == "4":

        student_id = int(input("Student ID : "))
        course = input("Course Name : ")

        drop_course(student_id, course)

    elif choice == "5":

        delete_student(
            int(input("Student ID : "))
        )

    elif choice == "6":

        save_students(students)

    elif choice == "7":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")