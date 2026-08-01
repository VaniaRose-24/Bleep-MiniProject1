import csv
from models.payroll import Payroll


def save_employees(employees):

    with open("data/employees.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "BasicSalary"]
        )

        for employee in employees:

            writer.writerow(
                [
                    employee.get_id(),
                    employee.get_name(),
                    employee.get_salary()
                ]
            )

    print("Employees Saved Successfully")


def load_employees():

    employees = []

    try:

        with open("data/employees.csv", "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                return employees

            for row in rows[1:]:

                employees.append(

                    Payroll(

                        int(row[0]),
                        row[1],
                        float(row[2])

                    )

                )

    except FileNotFoundError:

        pass

    return employees