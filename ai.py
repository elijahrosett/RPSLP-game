import random
from player import Player
class Ai(Player):
    def __init__(self,name):
        self.gesture = None
        super().__init__(name)

    def gesture_pick(self):
        self.gesture = random.choice(self.gesture_list)
        print(f"{self.name} has picked {self.gesture}!")
        

