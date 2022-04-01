import random

class Apartment():

  def __init__(self):
    # super().__init__()
    self.balcony = random.choice(['Yes', 'No'])
    self.laundry = random.choice(['Yes', 'No'])

  # Print results of what is stored in this object
  def display(self):
    print("Has Balcony: {}".format(self.balcony))
    print("Has Laundry: {}".format(self.laundry))
