__author__ = "Silvia Nittel"
__copyright__ = "Copyright 2022, SIE508, University of Maine"
__credits__ = ["Richard Twiggs"]
__what__ = "This is Homework Assignment 4"

from Realtor import Realtor
from Property import Property
import random

property_count = 0

print("Agent   Rent     Property Type   Address")

while property_count < 3:
  agent = Realtor()
  agent.listproperties()

  # Increment for next property
  property_count += 1
