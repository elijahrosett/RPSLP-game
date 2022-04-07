from human import Human
from ai import Ai
class Arena:
    def __init__(self):
        self.player_one = None
        self.player_two = None
    def run_game(self):
        self.greeting()
        self.how_many_players()
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.play_round()
        self.display_winner()
    def greeting(self):
        print("Welcome to rock, paper, scissors, Spock, lizard!")
    def how_many_players(self):
        user_input = input("How many people will be playing?")
        if user_input == '1':
            self.player_two = Ai("Jarvis")
            self.player_one = Human(input("Please enter player one's name"))
            print(f"Welcome {self.player_one.name}! You will be playing againt {self.player_two.name}.")    
        elif user_input == '2':
            self.player_one = Human(input("Please enter player one's name"))
            self.player_two = Human(input("Please enter player two's name"))  
            print(f"Welcome {self.player_one.name} and {self.player_two.name}!")
        else:
            print('Invalid Input please type 1 or 2')
            self.how_many_players()
    def play_round(self):
        self.player_one.gesture_pick()
        self.player_two.gesture_pick()
        self.gesture_decider()
        print(f'{self.player_one.name} has a score of {self.player_one.score}')
        print(f'{self.player_two.name} has a score of {self.player_two.score}')
    def display_winner(self):
        if self.player_one.score >= 2:
            print(f'{self.player_one.name} Wins!')
        elif self.player_two.score >= 2:
            print(f'{self.player_two.name} Wins!')
    def gesture_decider(self):
        if self.player_one.gesture == self.player_two.gesture:
            print(f'{self.player_one.gesture} ties with {self.player_two.gesture}')
            print(f'Both players used {self.player_one.gesture} and tied!')
        elif self.player_one.gesture == 'rock' and self.player_two.gesture == 'scissors':
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'scissors' and self.player_two.gesture == 'paper':
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'paper' and self.player_two.gesture == "rock":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'rock' and self.player_two.gesture == "lizard":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'lizard' and self.player_two.gesture == "spock":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'spock' and self.player_two.gesture == "scissors":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'scissors' and self.player_two.gesture == "lizard":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'lizard' and self.player_two.gesture == "paper":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'paper' and self.player_two.gesture == "spock":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        elif self.player_one.gesture == 'spock' and self.player_two.gesture == "rock":
            self.player_one.score += 1
            print(f'{self.player_one.gesture} beats {self.player_two.gesture}')
        else:
            print(f'{self.player_two.gesture} beats {self.player_one.gesture}')
            self.player_two.score += 1
