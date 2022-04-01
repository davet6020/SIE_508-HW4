from Property import Property


class House(Property):

  def __init__(self):
    # super().__init__()
    self.num_stories = None
    self.garage = None
    self.fenced_yard = None
    self.initializeproperty()

  # Ask user for input
  def initializeproperty(self):
    self.num_stories = int(input("How many stories is this house: "))
    self.garage = input("Does this house have a garage: ")
    self.fenced_yard = input("Does this house have a fenced yard: ")

    # Basic error checking to force the result into a No or Yes
    if self.garage.upper() == "N" or int(self.garage == 0):
      self.garage = "No"
    else:
      self.garage = "Yes"

    # Basic error checking to force the result into a No or Yes
    if self.fenced_yard.upper() == "N" or int(self.fenced_yard == 0):
      self.fenced_yard = "No"
    else:
      self.fenced_yard = "Yes"

  # Print results of what is stored in this object
  def display(self):
    print("Number of stories: {}".format(self.num_stories))
    print("Has Garage: {}".format(self.garage))
    print("Has Fenced in yard: {}".format(self.fenced_yard))
