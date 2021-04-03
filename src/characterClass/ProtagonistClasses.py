from .CharacterClass import CharacterClass


class Wizard(CharacterClass):
    def __init__(self):
        super().__init__("Wizard", 6, 10)
        self._mana = 10


class Monk(CharacterClass):
    def __init__(self):
        super().__init__("Monk", 6, 14)
        self._ki = 3


class Barbarian(CharacterClass):
    def __init__(self):
        super().__init__("Barbarian", 12, 10)


class Archer(CharacterClass):
    def __init__(self):
        super().__init__("Archer", 8, 10)
