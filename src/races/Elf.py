from characterRace import characterRace


class Elf():
    def __init__(self):
        self.elf = characterRace("Elf", 35, "Wisdom", "Dex")

    def printElf(self):
        self.elf.printRace()


testing = Elf()
testing.printElf()