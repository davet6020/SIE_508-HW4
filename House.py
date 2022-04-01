import random

class House():

  def __init__(self):
    # super().__init__()
    self.num_stories = random.randint(0, 5)
    self.garage = random.choice(['Yes', 'No'])
    self.fenced_yard = random.choice(['Yes', 'No'])

  # Print results of what is stored in this object
  def display(self):
    print("Number of stories: {}".format(self.num_stories))
    print("Has Garage: {}".format(self.garage))
    print("Has Fenced in yard: {}".format(self.fenced_yard))
