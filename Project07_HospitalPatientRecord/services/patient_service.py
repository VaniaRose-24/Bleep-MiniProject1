from models.patient import Patient

patients = []


def add_patient(patient_id, name, age, disease):

    patients.append(
        Patient(patient_id, name, age, disease)
    )

    print("Patient Registered Successfully")


def display_patients():

    if not patients:
        print("No Patients Found")
        return

    for patient in patients:
        patient.display()


def search_patient(patient_id):

    for patient in patients:

        if patient.get_id() == patient_id:
            return patient

    return None


def update_patient(patient_id):

    patient = search_patient(patient_id)

    if patient:

        name = input("New Name : ")
        age = int(input("New Age : "))
        disease = input("New Disease : ")

        patient.set_name(name)
        patient.set_age(age)
        patient.set_disease(disease)

        print("Patient Updated Successfully")

    else:

        print("Patient Not Found")


def delete_patient(patient_id):

    global patients

    for patient in patients:

        if patient.get_id() == patient_id:

            patients.remove(patient)

            print("Patient Deleted Successfully")

            return

    print("Patient Not Found")