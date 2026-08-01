from services.employee_service import *
from services.file_service import *

from services.employee_service import employees

employees.extend(load_employees())

while True:

    print("""
========= EMPLOYEE PAYROLL SYSTEM =========

1. Add Employee
2. Display Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Generate Payslip
7. Save Employees
8. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        emp_id = int(input("Employee ID : "))
        name = input("Employee Name : ")
        salary = float(input("Basic Salary : "))

        add_employee(emp_id, name, salary)

    elif choice == "2":

        display_employees()

    elif choice == "3":

        emp_id = int(input("Employee ID : "))

        employee = search_employee(emp_id)

        if employee:
            employee.display()
        else:
            print("Employee Not Found")

    elif choice == "4":

        update_employee(int(input("Employee ID : ")))

    elif choice == "5":

        delete_employee(int(input("Employee ID : ")))

    elif choice == "6":

        emp_id = int(input("Employee ID : "))

        employee = search_employee(emp_id)

        if employee:
            employee.display()
        else:
            print("Employee Not Found")

    elif choice == "7":

        save_employees(employees)

    elif choice == "8":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")