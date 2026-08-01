from models.expense import Expense

records = []


def add_record(record_id, category, amount, record_type):

    records.append(
        Expense(record_id, category, amount, record_type)
    )

    print("Record Added Successfully")


def display_records():

    if not records:
        print("No Records Found")
        return

    for record in records:
        record.display()


def search_record(record_id):

    for record in records:

        if record.get_id() == record_id:
            return record

    return None


def update_record(record_id):

    record = search_record(record_id)

    if record:

        category = input("New Category : ")
        amount = float(input("New Amount : "))
        record_type = input("New Type (Income/Expense) : ")

        record.set_category(category)
        record.set_amount(amount)
        record.set_type(record_type)

        print("Record Updated Successfully")

    else:

        print("Record Not Found")


def delete_record(record_id):

    global records

    for record in records:

        if record.get_id() == record_id:

            records.remove(record)

            print("Record Deleted Successfully")

            return

    print("Record Not Found")


def monthly_summary():

    income = 0
    expense = 0

    for record in records:

        if record.get_type().lower() == "income":
            income += record.get_amount()
        else:
            expense += record.get_amount()

    print("\nMonthly Summary")
    print("Income :", income)
    print("Expense:", expense)
    print("Balance:", income - expense)