from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, vehicle_id, name, rent_per_day):
        self.__vehicle_id = vehicle_id
        self.__name = name
        self.__rent_per_day = rent_per_day
        self.__available = True

    def get_id(self):
        return self.__vehicle_id

    def get_name(self):
        return self.__name

    def get_rent(self):
        return self.__rent_per_day

    def is_available(self):
        return self.__available

    def rent(self):
        self.__available = False

    def return_vehicle(self):
        self.__available = True

    @abstractmethod
    def display(self):
        pass