from gesture import Gesture
class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'lizard'
        self.can_beat = ['spock', 'paper']
