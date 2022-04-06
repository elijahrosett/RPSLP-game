class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "Spock"]
        self.score = 0

    def gesture_pick(self):
        self.gesture = input("Which gesture would you like to do?")
        if self.gesture in self.gesture_list:
            print(f"You have picked {self.gesture}!")
        else:
            print(f"{self.gesture} is not a valid input")
            self.gesture_pick()

