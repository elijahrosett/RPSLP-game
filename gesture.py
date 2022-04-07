class Gesture:
    def __init__(self, name, can_beat, is_beat_by):
        self.name = name
        self.can_beat = can_beat
        self.is_beat_by = is_beat_by
    def gesture_check(self, compare):
        if compare in self.can_beat:
            return 1
        elif compare in self.is_beat_by:
            return 2
        else:
            return 0