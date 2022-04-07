from gesture import Gesture
from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock
rock = Gesture('Rock', ['Scissors', 'Lizard'], ['Spock', 'Paper'])
paper = Gesture('Paper', ['Rock', 'Spock'], ['Scissors', 'Lizard'])
scissors = Gesture('Scissors', ['Paper', 'Lizard'], ['Rock', 'Spock'])
lizard = Gesture('Lizard', ['Paper', 'Spock'], ['Scissors', 'Rock'])
spock = Gesture('Spock', ['Rock', 'Scissors'], ['Lizard', 'Paper'])

class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_list = [rock, paper, scissors, lizard, spock]
        self.score = 0
    def gesture_pick(self):
        print('rock = 0')
        print('paper = 1')
        print('scissors = 2')
        print('lizard = 3')
        print('spock = 4')
        self.gesture_input = int(input("Which gesture would you like to do?"))
        if self.gesture_input in range(0, 5):
            self.gesture = self.gesture_list[self.gesture_input]
            print(f'You played {self.gesture.name}')
        else:
            print('Invalid Input, Try Again')
            self.gesture_pick()

