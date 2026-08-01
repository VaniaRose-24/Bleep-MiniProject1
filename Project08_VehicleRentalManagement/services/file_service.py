import csv
from models.rental import Rental


def save_vehicles(vehicles):

    with open("data/vehicles.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Rent", "Available"]
        )

        for vehicle in vehicles:

            writer.writerow(
                [
                    vehicle.get_id(),
                    vehicle.get_name(),
                    vehicle.get_rent(),
                    vehicle.is_available()
                ]
            )

    print("Vehicles Saved Successfully")


def load_vehicles():

    vehicles = []

    try:

        with open("data/vehicles.csv", "r") as file:

            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                return vehicles

            for row in rows[1:]:

                vehicle = Rental(
                    int(row[0]),
                    row[1],
                    float(row[2])
                )

                if row[3] == "False":
                    vehicle.rent()

                vehicles.append(vehicle)

    except FileNotFoundError:

        pass

    return vehicles