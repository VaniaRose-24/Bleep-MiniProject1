import csv
from models.expense import Expense


def save_records(records):

    with open("data/expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Category", "Amount", "Type"]
        )

        for record in records:

            writer.writerow([
                record.get_id(),
                record.get_category(),
                record.get_amount(),
                record.get_type()
            ])

    print("Records Saved Successfully")


def load_records():

    records = []

    try:

        with open("data/expenses.csv", "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                return records

            for row in rows[1:]:

                records.append(

                    Expense(

                        int(row[0]),
                        row[1],
                        float(row[2]),
                        row[3]

                    )

                )

    except FileNotFoundError:

        pass

    return records