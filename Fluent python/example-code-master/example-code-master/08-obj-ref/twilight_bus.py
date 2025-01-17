"""
>>> basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
>>> bus = TwilightBus(basketball_team)
>>> bus.drop('Tina')
>>> bus.drop('Pat')
>>> basketball_team
['Sue', 'Maya', 'Diana']
"""

# BEGIN TWILIGHT_BUS_CLASS
class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        self.passengers = [] if passengers is None else passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>
# END TWILIGHT_BUS_CLASS

