from unicodedata import name
from player import Player

class Human(Player):
    def __init__(self, name):
        self.genture = None
        super().__init__(name)