from Property import Property


class Apartment(Property):

  def __init__(self):
    # super().__init__()
    self.balcony = None
    self.laundry = None
    self.initializeproperty()

  # Ask user for input
  def initializeproperty(self):
    self.balcony = input("Does this apartment have a balcony: ")
    self.laundry = input("Does this apartment have a laundry facility: ")

    # Basic error checking to force the result into a No or Yes
    if self.balcony.upper() == "N" or int(self.balcony == 0):
      self.balcony = "No"
    else:
      self.balcony = "Yes"

    # Basic error checking to force the result into a No or Yes
    if self.laundry.upper() == "N" or int(self.laundry == 0):
      self.laundry = "No"
    else:
      self.laundry = "Yes"

  # Print results of what is stored in this object
  def display(self):
    print("Has Balcony: {}".format(self.balcony))
    print("Has Laundry: {}".format(self.laundry))
