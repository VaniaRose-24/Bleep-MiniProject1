from services.patient_service import *
from services.file_service import *

from services.patient_service import patients

patients.extend(load_patients())

while True:

    print("""
========= HOSPITAL PATIENT RECORD SYSTEM =========

1. Register Patient
2. Display Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Save Records
7. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        patient_id = int(input("Patient ID : "))
        name = input("Patient Name : ")
        age = int(input("Age : "))
        disease = input("Disease : ")

        add_patient(patient_id, name, age, disease)

    elif choice == "2":

        display_patients()

    elif choice == "3":

        patient = search_patient(
            int(input("Patient ID : "))
        )

        if patient:
            patient.display()
        else:
            print("Patient Not Found")

    elif choice == "4":

        update_patient(
            int(input("Patient ID : "))
        )

    elif choice == "5":

        delete_patient(
            int(input("Patient ID : "))
        )

    elif choice == "6":

        save_patients(patients)

    elif choice == "7":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")