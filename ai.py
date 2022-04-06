from player import Player
class AI(Player):
    def __init__(self,name):
        self.name = "Jarivs"
        self.select_gesture = ""
        super().__init__(name)