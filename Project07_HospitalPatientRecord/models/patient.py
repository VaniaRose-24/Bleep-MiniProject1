from models.person import Person

class Patient(Person):

    def __init__(self, patient_id, name, age, disease):
        super().__init__(patient_id, name, age)
        self.__disease = disease

    def get_disease(self):
        return self.__disease

    def set_disease(self, disease):
        self.__disease = disease

    def display(self):

        print("----------------------------")
        print("Patient ID :", self.get_id())
        print("Name       :", self.get_name())
        print("Age        :", self.get_age())
        print("Disease    :", self.__disease)
        print("----------------------------")