from characterRace import characterRace


class Elf(characterRace):
    def __init__(self):
        super().__init__("Human", 30, "Dexterity", "Charisma")
