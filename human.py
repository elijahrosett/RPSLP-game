from player import Player

class Human(Player):
    def __init__(self,name):
        self.name = input("Enter your name")
        self.select_gesture = ""
        super().__init__(name)