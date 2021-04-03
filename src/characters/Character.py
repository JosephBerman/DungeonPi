from src.characterClass.ProtagonistClasses import *
from src.races.ProtagonistRaces import *


class Character:
    def __init__(self):
        self.characterRace = Human()  # going to make a race class
        self.characterClass = Archer()  # going to make a class class

    def printCharacter(self):
        self.characterRace.printRace()
        self.characterClass.printClass()


