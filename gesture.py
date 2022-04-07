class Gesture:
    def __init__(self):
        self.name = None
        self.can_beat = None
        self.is_beat_by = None
    def gesture_check(self, compare):
        if compare in self.can_beat:
            return 1
        elif compare in self.is_beat_by:
            return 2
        else:
            return 0