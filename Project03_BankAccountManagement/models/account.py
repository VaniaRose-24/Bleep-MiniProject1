from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_no, holder_name, balance=0):
        self.__account_no = account_no
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_no(self):
        return self.__account_no

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return False
        self.__balance -= amount
        return True

    @abstractmethod
    def display(self):
        pass