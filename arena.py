class arena:
    def __init__(self):
        self.player_one = ""
        self.player_two = None

    def run_game(self):
        pass

    
    def greeting(self):
        print("Welcome to rock, paper, scissors, Spock, lizard!")

    def how_many_players(self):
        user_input = int(input("How many player?"))
        if user_input == 1:
            self.player_two = AI
        elif user_input == 2:
            self.player_two = human    

    def play_round(self):

        pass




#greeting
#how many players?
#if 1 player_two = human
#elif 2 player_two = ai