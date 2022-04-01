from Property import Property
import random

class RealEstateAgent:
  property_list = {}

  def __init__(self):
    self.agent = random.choice(['Avery', 'Jewell', 'Rose', 'Tom'])
    self.propertiid = None
    self.address = None
    self.property_type = None
    self.rent = None
    self.none = None

  def listproperties(self, agent):
    self.none = None
    print("Agent - Rent - Property Type - Address")
    for pid, pinfo in RealEstateAgent.property_list.items():
      if pinfo['agent'] == agent:
        print("{: <7} {: <6} {: <15} {: <30}".format(pinfo['agent'], pinfo['rent'], pinfo['property_type'],
                                                     pinfo['address']))

  # Store the assigned values to this agents object
  def addproperty(self, agent, propertiid,  address, property_type, rent):
    self.agent = agent
    self.propertiid = propertiid
    self.address = address
    self.property_type = property_type
    self.rent = rent

    # Put the property values onto the Agent object
    RealEstateAgent.pr = {'agent': self.agent, 'address': self.address,
                          'property_type': self.property_type, 'rent': self.rent}
    RealEstateAgent.property_list[self.propertiid] = RealEstateAgent.pr
