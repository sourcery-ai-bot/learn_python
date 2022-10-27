
"""
>>> import copy
>>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
>>> bus2 = copy.copy(bus1)
>>> bus3 = copy.deepcopy(bus1)
>>> bus1.drop('Bill')
>>> bus2.passengers
['Alice', 'Claire', 'David']
>>> bus3.passengers
['Alice', 'Bill', 'Claire', 'David']

"""

# BEGIN BUS_CLASS
class Bus:

    def __init__(self, passengers=None):
        self.passengers = [] if passengers is None else list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
# END BUS_CLASS
