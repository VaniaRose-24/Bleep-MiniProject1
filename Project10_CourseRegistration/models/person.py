from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def display(self):
        pass