from .CharacterRace import CharacterRace


class Elf(CharacterRace):
    def __init__(self):
        super().__init__("Elf", 35, "Wisdom", "Dexterity")


class Human(CharacterRace):
    def __init__(self):
        super().__init__("Human", 30, "Dexterity", "Charisma")
