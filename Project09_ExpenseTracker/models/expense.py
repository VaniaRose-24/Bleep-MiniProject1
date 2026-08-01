from models.record import Record

class Expense(Record):

    def __init__(self, record_id, category, amount, record_type):
        super().__init__(record_id, category, amount)
        self.__record_type = record_type

    def get_type(self):
        return self.__record_type

    def set_type(self, record_type):
        self.__record_type = record_type

    def display(self):

        print("-----------------------------")
        print("Record ID :", self.get_id())
        print("Type      :", self.__record_type)
        print("Category  :", self.get_category())
        print("Amount    :", self.get_amount())
        print("-----------------------------")