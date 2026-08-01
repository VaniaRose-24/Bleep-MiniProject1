from services.student_services import *
from services.file_services import save_students
from utils.validator import *
from models.grade import Grade

while True:

    print("""
========== STUDENT MANAGEMENT ==========
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Average Marks
7. Topper
8. Save Records
9. Exit
""")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Name: ")
        age = get_int("Age: ")
        roll = get_int("Roll: ")
        marks = get_float("Marks: ")

        add_student(name, age, roll, marks)

        print("Grade:", Grade.calculate_grade(marks))

    elif choice == "2":

        display_students()

    elif choice == "3":

        roll = get_int("Roll: ")

        search_student(roll)

    elif choice == "4":

        roll = get_int("Enter Roll: ")

        name = input("New Name: ")
        age = get_int("New Age: ")
        marks = get_float("New Marks: ")

        update_student(roll, name, age, marks)

    elif choice == "5":

        roll = get_int("Roll: ")

        delete_student(roll)

    elif choice == "6":

        print("Average =", average_marks())

    elif choice == "7":

        student = topper()

        if student:
            print("\nTopper")
            student.display()

    elif choice == "8":

        save_students(students)

        print("Saved Successfully")

    elif choice == "9":

        break

    else:

        print("Invalid Choice")