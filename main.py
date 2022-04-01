__author__ = "Silvia Nittel"
__copyright__ = "Copyright 2022, SIE508, University of Maine"
__credits__ = ["Richard Twiggs"]
__what__ = "This is Homework Assignment 3"

from RealEstateAgent import RealEstateAgent
from Property import Property
from House import House
from Apartment import Apartment
import random

mls = {}
property_count = 0

# Instantiate two realtor objects
agent1 = RealEstateAgent()
agent2 = RealEstateAgent()

# Have user input 3 properties
print("Input Three Properties")
while property_count < 3:
  # By instantiating a Property object, you call Property.initializeproperty which asks for input
  p = Property()

  # Loop through p items() and put them into a dictionary for use in assigning the property to a realtor
  for attr, value in p.__dict__.items():
    if attr == 'address':
      mls['address'] = value
    if attr == 'rent':
      mls['rent'] = value

  # Determine if Apartment or House and call that Class.initializeproperty method
  AorH = input("Is this an Apartment or a House (A or H): ")
  if AorH.upper() == "A":
    a = Apartment()
    # We need the property type for assigning it to the realtor
    mls['property_type'] = 'Apartment'
  else:
    h = House()
    # We need the property type for assigning it to the realtor
    mls['property_type'] = 'House'

  # Time to assign property to realtor
  if (property_count % 2) == 0:
    agent1.addproperty('Jewel', property_count, mls['address'], mls['property_type'], mls['rent'])
  else:
    agent2.addproperty('Tom', property_count, mls['address'], mls['property_type'], mls['rent'])

  # Increment for next property
  property_count += 1

# Print out a list of all agents properties
agent1.listproperties('Tom')
agent2.listproperties('Jewel')
