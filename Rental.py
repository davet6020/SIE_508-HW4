from ApartmentRental import ApartmentRental
from HouseRental import HouseRental


class Rental(HouseRental, ApartmentRental):

    def __init__(self):
        self.rent = 0.00

    def display(self):
        pass
