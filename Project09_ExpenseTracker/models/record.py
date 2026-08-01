from abc import ABC, abstractmethod

class Record(ABC):

    def __init__(self, record_id, category, amount):
        self.__record_id = record_id
        self.__category = category
        self.__amount = amount

    def get_id(self):
        return self.__record_id

    def get_category(self):
        return self.__category

    def get_amount(self):
        return self.__amount

    def set_category(self, category):
        self.__category = category

    def set_amount(self, amount):
        self.__amount = amount

    @abstractmethod
    def display(self):
        pass