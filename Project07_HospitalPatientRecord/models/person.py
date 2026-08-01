from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, patient_id, name, age):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age

    def get_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    @abstractmethod
    def display(self):
        pass