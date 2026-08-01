from services.rental_service import *
from services.file_service import *

from services.rental_service import vehicles

vehicles.extend(load_vehicles())

while True:

    print("""
========= VEHICLE RENTAL MANAGEMENT =========

1. Add Vehicle
2. Display Vehicles
3. Search Vehicle
4. Rent Vehicle
5. Return Vehicle
6. Calculate Charges
7. Delete Vehicle
8. Save Records
9. Exit

""")

    choice = input("Enter Choice : ")

    if choice == "1":

        vehicle_id = int(input("Vehicle ID : "))
        name = input("Vehicle Name : ")
        rent = float(input("Rent Per Day : "))

        add_vehicle(vehicle_id, name, rent)

    elif choice == "2":

        display_vehicles()

    elif choice == "3":

        vehicle = search_vehicle(
            int(input("Vehicle ID : "))
        )

        if vehicle:
            vehicle.display()
        else:
            print("Vehicle Not Found")

    elif choice == "4":

        rent_vehicle(
            int(input("Vehicle ID : "))
        )

    elif choice == "5":

        return_vehicle(
            int(input("Vehicle ID : "))
        )

    elif choice == "6":

        vehicle_id = int(input("Vehicle ID : "))
        days = int(input("Number of Days : "))

        calculate_charge(vehicle_id, days)

    elif choice == "7":

        delete_vehicle(
            int(input("Vehicle ID : "))
        )

    elif choice == "8":

        save_vehicles(vehicles)

    elif choice == "9":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")