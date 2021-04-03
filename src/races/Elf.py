from characterRace import characterRace


class Elf(characterRace):
    def __init__(self):
        super().__init__("Elf", 35, "Wisdom", "Dexterity")


testing = Elf()
testing.printRace()
