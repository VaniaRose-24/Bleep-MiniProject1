from models.rental import Rental

vehicles = []


def add_vehicle(vehicle_id, name, rent):

    vehicles.append(Rental(vehicle_id, name, rent))

    print("Vehicle Added Successfully")


def display_vehicles():

    if not vehicles:
        print("No Vehicles Found")
        return

    for vehicle in vehicles:
        vehicle.display()


def search_vehicle(vehicle_id):

    for vehicle in vehicles:

        if vehicle.get_id() == vehicle_id:
            return vehicle

    return None


def rent_vehicle(vehicle_id):

    vehicle = search_vehicle(vehicle_id)

    if vehicle:

        if vehicle.is_available():

            vehicle.rent()

            print("Vehicle Rented Successfully")

        else:

            print("Vehicle Already Rented")

    else:

        print("Vehicle Not Found")


def return_vehicle(vehicle_id):

    vehicle = search_vehicle(vehicle_id)

    if vehicle:

        vehicle.return_vehicle()

        print("Vehicle Returned Successfully")

    else:

        print("Vehicle Not Found")


def calculate_charge(vehicle_id, days):

    vehicle = search_vehicle(vehicle_id)

    if vehicle:

        print(f"Total Charge : ₹{vehicle.get_rent() * days}")

    else:

        print("Vehicle Not Found")


def delete_vehicle(vehicle_id):

    global vehicles

    for vehicle in vehicles:

        if vehicle.get_id() == vehicle_id:

            vehicles.remove(vehicle)

            print("Vehicle Deleted Successfully")

            return

    print("Vehicle Not Found")