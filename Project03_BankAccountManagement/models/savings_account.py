from models.account import Account

class SavingsAccount(Account):

    def display(self):
        print("-----------------------------")
        print("Account No :", self.get_account_no())
        print("Holder     :", self.get_holder_name())
        print("Balance    :", self.get_balance())
        print("-----------------------------")