import random
from player import Player
class AI(Player):
    def __init__(self,name):
        self.name = "Jarivs"
        self.select_gesture = ""
        super().__init__(name)

    def gesture_pick(self):
        self.gesture = random.choice(self.gesture_list)
        print(f"{self.name} has picked {self.gesture}!")
        

ai = AI("Jarvis")
ai.gesture_pick()