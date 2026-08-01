from abc import ABC, abstractmethod

class Item(ABC):

    def __init__(self, item_id, title):
        self.__item_id = item_id
        self.__title = title

    def get_id(self):
        return self.__item_id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    @abstractmethod
    def display(self):
        pass