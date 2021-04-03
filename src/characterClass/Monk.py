from CharacterClass import CharacterClass


class Monk(CharacterClass):
    def __init__(self):
        super().__init__("Monk", 6, 14)
        self.ki = 3



