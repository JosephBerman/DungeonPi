from CharacterClass import CharacterClass


class Wizard(CharacterClass):
    def __init__(self):
        super().__init__("Wizard", 6, 10)
        self._mana = 10


