from Property import Property
import random

class Realtor:
    property_list = {}
    property_count = 0

    def __init__(self):
        self.mls = {}
        self.agent = random.choice(['Avery', 'Jewell', 'Rose', 'Tom'])
        self.none = None
        self.addproperty()

    # Store the assigned values to this agents object
    def addproperty(self):
        self.none = None

        p = Property()

        # Loop through p items() and put them into a dictionary for use in assigning the property to a realtor
        for attr, value in p.__dict__.items():
            # print('a: {} === v: {}'.format(attr, value))
            if attr == 'address':
                self.mls['address'] = value
            if attr == 'rent':
                self.mls['rent'] = value
            if attr == 'property_type':
                self.mls['property_type'] = value
            if attr == 'property_count':
                self.mls['property_count'] = value

    def listproperties(self):
        self.mls['agent'] = self.agent
        # print("Agent - Rent - Property Type - Address")
        print("{: <7} {: <8} {: <15} {: <30}".format(self.mls['agent'], self.mls['rent'], self.mls['property_type'],
                                                     self.mls['address']))
