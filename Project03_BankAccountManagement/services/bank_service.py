from models.savings_account import SavingsAccount
from models.transaction import Transaction

accounts = []
transactions = []


def create_account(account_no, holder_name, balance):

    account = SavingsAccount(account_no, holder_name, balance)

    accounts.append(account)

    print("Account Created Successfully")


def search_account(account_no):

    for account in accounts:

        if account.get_account_no() == account_no:

            return account

    return None


def deposit(account_no, amount):

    account = search_account(account_no)

    if account:

        account.deposit(amount)

        transactions.append(
            Transaction(account_no, "Deposit", amount)
        )

        print("Deposit Successful")

    else:

        print("Account Not Found")


def withdraw(account_no, amount):

    account = search_account(account_no)

    if account:

        if account.withdraw(amount):

            transactions.append(
                Transaction(account_no, "Withdraw", amount)
            )

            print("Withdrawal Successful")

        else:

            print("Insufficient Balance")

    else:

        print("Account Not Found")


def display_accounts():

    if not accounts:

        print("No Accounts Found")

        return

    for account in accounts:

        account.display()


def transaction_history(account_no):

    found = False

    for transaction in transactions:

        if transaction.account_no == account_no:

            transaction.display()

            found = True

    if not found:

        print("No Transactions Found")


def delete_account(account_no):

    global accounts

    for account in accounts:

        if account.get_account_no() == account_no:

            accounts.remove(account)

            print("Account Deleted")

            return

    print("Account Not Found")