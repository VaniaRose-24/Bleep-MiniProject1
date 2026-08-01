from models.person import Person

class Student(Person):

    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.__courses = []

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def drop_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)

    def get_courses(self):
        return self.__courses

    def display(self):

        print("----------------------------")
        print("Student ID :", self.get_id())
        print("Name       :", self.get_name())
        print("Courses    :", ", ".join(self.__courses) if self.__courses else "None")
        print("----------------------------")