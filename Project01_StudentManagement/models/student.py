from models.person import Person

class Student(Person):

    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.__roll = roll
        self.__marks = marks

    def get_roll(self):
        return self.__roll

    def set_roll(self, roll):
        self.__roll = roll

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print(
            self.get_roll(),
            self.get_name(),
            self.get_age(),
            self.get_marks()
        )