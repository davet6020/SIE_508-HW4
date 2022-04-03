from House import House
from Apartment import Apartment
import random

class Property:

  def __init__(self):
    self.square_feet = int(random.randint(900, 5000))
    self.num_bedrooms = int(self.square_feet / 1500)
    self.num_bathrooms = int(self.square_feet / 1200)
    self.rent = "{:.2f}".format(self.square_feet * 1.05)
    self.property_type = random.choice(['Apartment', 'House'])
    self.rent_own = random.choice(['Purchase', 'Rent'])

    if self.property_type == "Apartment":
      self.ptype_info = Apartment()
      self.unit = random.choice(['Apt ', 'Unit ', ''])
      self.unit_info = self.unit + random.choice(['14G', '3C', 'J13', '221b', '10D', '42', '666', 'L7', '9'])
    else:
      self.ptype_info = House()
      self.unit_info = ''

    self.street_num = str(random.randint(1, 5000))
    self.street_name = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']) + ' St.'
    self.street_city = 'Washington, DC'
    self.zip_code = int(random.randint(20001, 20012))
    self.address = '{} {} {} {} {}'.format(self.street_num, self.street_name, self.unit_info, self.street_city, self.zip_code)

  # Print results of what is stored in this object
  def display(self):
    print("Property Type: {}".format(self.property_type))
    print("Square Footage: {}".format(self.square_feet))
    print("Number of Bedrooms: {}".format(self.num_bedrooms))
    print("Number of Bathrooms: {}".format(self.num_bathrooms))
    print("Rent: {}".format(self.rent))
    self.ptype_info.display()

  def gen_address(self):
    pass
