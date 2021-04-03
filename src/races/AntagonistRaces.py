from .CharacterRace import CharacterRace


class Goblin(CharacterRace):
    def __init__(self):
        super().__init__("Goblin", 30, "None", "None")
