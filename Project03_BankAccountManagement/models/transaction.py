class Transaction:

    def __init__(self, account_no, transaction_type, amount):
        self.account_no = account_no
        self.transaction_type = transaction_type
        self.amount = amount

    def display(self):
        print(
            f"{self.account_no} | "
            f"{self.transaction_type} | "
            f"{self.amount}"
        )