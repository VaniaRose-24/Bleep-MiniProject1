from models.question import Question

class Quiz(Question):

    def display(self):

        print("\n" + self.get_question())

        options = self.get_options()

        for i in range(4):
            print(f"{i+1}. {options[i]}")