from human import Human
from ai import Ai






class Arena:
    def __init__(self):
        self.player_one = ""
        self.player_two = ""
        

    def run_game(self):
        self.greeting()
        self.how_many_players
        pass


    def greeting(self):
        print("Welcome to rock, paper, scissors, Spock, lizard!")
        

    def how_many_players(self):
        user_input = int(input("How many people will be playing?"))
        if user_input == 1:
            self.player_two = Ai("Jarvis")
            self.player_one = Human(input("Please enter player one's name"))
            print(f"Welcome {self.player_one.name}! You will be playing againt {self.player_two.name}.")    
        elif user_input == 2:
            self.player_one = Human(input("Please enter player one's name"))
            self.player_two = Human(input("Please enter player two's name"))  
            print(f"Welcome {self.player_one.name} and {self.player_two.name}!")
    
    def play_round(self):
        
        pass

        pass

    def gesture_decider(self):
        if self.player_one.gesture == 'rock' and self.player_two.gesture == 'scissors':
            self.player_one.score += 1
        elif self.player_two.gesture == 'rock' and self.player_one.gesture == 'scissors':
            self.player_two.score += 1
        elif self.player_one.gesture == 'scissors' and self.player_two.gesture == 'paper':
            self.player_one.score += 1
        elif self.player_two.gesture == 'scissors' and self.player_one.gesture == 'paper':
            self.player_two.score += 1
        elif self.player_one.gesture == 'paper' and self.player_two.gesture == "rock":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'paper' and self.player_one.gesture == "rock":
            self.player_two.gesture += 1
        elif self.player_one.gesture == 'rock' and self.player_two.gesture == "lizard":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'rock' and self.player_one.gesture == "lizard":
            self.player_two.gesture += 1
        elif self.player_one.gesture == 'lizard' and self.player_two.gesture == "spock":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'lizard' and self.player_one.gesture == "spock":
            self.player_two.gesture += 1
        elif self.player_one.gesture == 'spock' and self.player_two.gesture == "scissors":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'spock' and self.player_one.gesture == "scissors":
            self.player_two.gesture += 1
        elif self.player_one.gesture == 'scissors' and self.player_two.gesture == "lizard":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'scissors' and self.player_two.gesture == "lizard":
            self.player_two.gesture += 1
        elif self.player_one.gesture == 'lizard' and self.player_two.gesture == "paper":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'lizard' and self.player_one.gesture == "paper":
            self.player_two.gesture += 1
        elif self.player_one.gesture == 'paper' and self.player_two.gesture == "spock":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'paper' and self.player_one.gesture == "spock":
            self.player_two.gesture += 1
        elif self.player_one.gesture == 'spock' and self.player_two.gesture == "rock":
            self.player_one.gesture += 1
        elif self.player_two.gesture == 'spock' and self.player_one.gesture == "rock":
            self.player_two.gesture += 1
        else:
            print(f'{self.player_one.gesture} ties with {self.player_two.gesture}')

            

test = Arena()
test.greeting()
test.how_many_players()
#greeting
#how many players?
#if 1 player_two = human
#elif 2 player_two = ai