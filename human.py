from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        self.select_gesture = ""
        super().__init__(name)