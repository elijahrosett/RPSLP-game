from gesture import Gesture
class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'scissors'
        self.can_beat = ['paper', 'lizard']
        self.is_beat_by = ['rock', 'spock']