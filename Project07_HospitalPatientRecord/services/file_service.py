import csv
from models.patient import Patient


def save_patients(patients):

    with open("data/patients.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Age", "Disease"]
        )

        for patient in patients:

            writer.writerow(
                [
                    patient.get_id(),
                    patient.get_name(),
                    patient.get_age(),
                    patient.get_disease()
                ]
            )

    print("Patients Saved Successfully")


def load_patients():

    patients = []

    try:

        with open("data/patients.csv", "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                return patients

            for row in rows[1:]:

                patients.append(

                    Patient(

                        int(row[0]),
                        row[1],
                        int(row[2]),
                        row[3]

                    )

                )

    except FileNotFoundError:

        pass

    return patients