from models.vehicle import Vehicle

class Rental(Vehicle):

    def display(self):

        status = "Available" if self.is_available() else "Rented"

        print("----------------------------")
        print("Vehicle ID :", self.get_id())
        print("Vehicle    :", self.get_name())
        print("Rent/Day   :", self.get_rent())
        print("Status     :", status)
        print("----------------------------")