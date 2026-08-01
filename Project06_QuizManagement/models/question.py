from abc import ABC, abstractmethod

class Question(ABC):

    def __init__(self, question, options, answer):
        self.__question = question
        self.__options = options
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_options(self):
        return self.__options

    def get_answer(self):
        return self.__answer

    @abstractmethod
    def display(self):
        pass