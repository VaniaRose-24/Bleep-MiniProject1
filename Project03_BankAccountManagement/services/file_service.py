import csv

from models.savings_account import SavingsAccount


def save_accounts(accounts):

    with open("data/accounts.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "AccountNo",
                "HolderName",
                "Balance"
            ]
        )

        for account in accounts:

            writer.writerow(
                [
                    account.get_account_no(),
                    account.get_holder_name(),
                    account.get_balance()
                ]
            )

    print("Accounts Saved Successfully")


def load_accounts():

    accounts = []

    try:

        with open("data/accounts.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:

                accounts.append(

                    SavingsAccount(

                        int(row[0]),

                        row[1],

                        float(row[2])

                    )

                )

    except FileNotFoundError:

        pass

    return accounts