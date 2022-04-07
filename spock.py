from gesture import Gesture
class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'spock'
        self.can_beat = ['scissors', 'lizard']
        self.is_beat_by = ['lizard', 'paper']