from services.expense_service import *
from services.file_service import *

from services.expense_service import records

records.extend(load_records())

while True:

    print("""
========== EXPENSE TRACKER ==========

1. Add Record
2. Display Records
3. Search Record
4. Update Record
5. Delete Record
6. Monthly Summary
7. Save Records
8. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        record_id = int(input("Record ID : "))
        category = input("Category : ")
        amount = float(input("Amount : "))
        record_type = input("Type (Income/Expense) : ")

        add_record(record_id, category, amount, record_type)

    elif choice == "2":

        display_records()

    elif choice == "3":

        record = search_record(
            int(input("Record ID : "))
        )

        if record:
            record.display()
        else:
            print("Record Not Found")

    elif choice == "4":

        update_record(
            int(input("Record ID : "))
        )

    elif choice == "5":

        delete_record(
            int(input("Record ID : "))
        )

    elif choice == "6":

        monthly_summary()

    elif choice == "7":

        save_records(records)

    elif choice == "8":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")