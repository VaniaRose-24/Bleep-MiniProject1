from services.bank_service import *
from services.file_service import save_accounts
from utils.validator import *

while True:

    print("""
========== BANK ACCOUNT MANAGEMENT ==========

1. Create Account
2. Deposit
3. Withdraw
4. Display Accounts
5. Transaction History
6. Delete Account
7. Save Accounts
8. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        account_no = get_int("Account Number : ")
        holder = input("Account Holder : ")
        balance = get_float("Opening Balance : ")

        create_account(account_no, holder, balance)

    elif choice == "2":

        account_no = get_int("Account Number : ")
        amount = get_float("Deposit Amount : ")

        deposit(account_no, amount)

    elif choice == "3":

        account_no = get_int("Account Number : ")
        amount = get_float("Withdraw Amount : ")

        withdraw(account_no, amount)

    elif choice == "4":

        display_accounts()

    elif choice == "5":

        account_no = get_int("Account Number : ")

        transaction_history(account_no)

    elif choice == "6":

        account_no = get_int("Account Number : ")

        delete_account(account_no)

    elif choice == "7":

        save_accounts(accounts)

    elif choice == "8":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")