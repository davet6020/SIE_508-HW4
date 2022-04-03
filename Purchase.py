from HousePurchase import HousePurchase
from HouseRental import HouseRental


class Purchase(HousePurchase, HouseRental):

    def __init__(self):
        self.price = 0.00
        self.taxes = 0.00

    def display(self):
        pass
