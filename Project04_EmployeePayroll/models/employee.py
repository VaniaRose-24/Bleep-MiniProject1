from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, emp_id, name, basic_salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__basic_salary = basic_salary

    def get_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__basic_salary

    def set_salary(self, salary):
        self.__basic_salary = salary

    @abstractmethod
    def display(self):
        pass