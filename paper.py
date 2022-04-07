from gesture import Gesture
class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'paper'
        self.can_beat = ['rock', 'spock']
        self.is_beat_by = ['scissors', 'lizard']