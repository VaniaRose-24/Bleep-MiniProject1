from models.item import Item

class Book(Item):

    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.__author = author
        self.__issued = False

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def is_issued(self):
        return self.__issued

    def issue(self):
        self.__issued = True

    def return_book(self):
        self.__issued = False

    def display(self):
        status = "Issued" if self.__issued else "Available"

        print(f"""
Book ID : {self.get_id()}
Title   : {self.get_title()}
Author  : {self.__author}
Status  : {status}
""")