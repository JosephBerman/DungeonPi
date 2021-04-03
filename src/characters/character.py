import src.characterClass.CharacterClass
import src.characterClass.Archer
import src.races.CharacterRace
import src.races.Human


class Character:
    def __init__(self):
        self.characterRace = src.races.Human.Human()  # going to make a race class
        self.characterClass = src.characterClass.Archer  # going to make a class class


testing = Character()


testing.characterRace.printRace()
testing.characterClass.printClass()