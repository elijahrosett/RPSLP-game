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
            print(f"Welcome {self.player_one.name}! You will be playing againt {self.player_two_ai.name}.")    
        elif user_input == 2:
            self.player_one = Human(input("Please enter player one's name"))
            self.player_two = Human(input("Please enter player two's name"))  
            print(f"Welcome {self.player_one.name} and {self.player_two.name}!")
    
    def play_round(self):
        
        pass

        pass

    def gesture_decider(self):

        pass


test = Arena()
test.greeting()
test.how_many_players()
#greeting
#how many players?
#if 1 player_two = human
#elif 2 player_two = ai