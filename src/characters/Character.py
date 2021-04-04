from src.characterClass.ProtagonistClasses import *
from src.races.ProtagonistRaces import *
from src.characters.Stats import *


class Character:
    def __init__(self, cr: CharacterRace, cc: CharacterClass, st: Stats):
        self._characterRace = cr
        self._characterClass = cc
        self._stats = st
        self._stats.statBonus1(self._characterRace.getStatBonus1())
        self._stats.statBonus2(self._characterRace.getStatBonus2())

    def printCharacter(self):
        self._characterRace.printRace()
        self._characterClass.printClass()
        self._stats.printStats()


testing = Character(Elf(), Monk(), Stats(1, 1, 1, 1, 1, 1))
testing.printCharacter()
