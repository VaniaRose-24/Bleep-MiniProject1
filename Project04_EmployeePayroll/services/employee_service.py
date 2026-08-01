from models.payroll import Payroll


employees = []


def add_employee(emp_id, name, salary):

    employees.append(Payroll(emp_id, name, salary))

    print("Employee Added Successfully")


def display_employees():

    if not employees:
        print("No Employees Found")
        return

    for employee in employees:
        employee.display()


def search_employee(emp_id):

    for employee in employees:

        if employee.get_id() == emp_id:
            return employee

    return None


def update_employee(emp_id):

    employee = search_employee(emp_id)

    if employee:

        name = input("New Name : ")
        salary = float(input("New Salary : "))

        employee._Employee__name = name
        employee.set_salary(salary)

        print("Employee Updated Successfully")

    else:

        print("Employee Not Found")


def delete_employee(emp_id):

    global employees

    for employee in employees:

        if employee.get_id() == emp_id:

            employees.remove(employee)

            print("Employee Deleted Successfully")

            return

    print("Employee Not Found")