from .CharacterRace import CharacterRace
from src.Constants import *

CONSTANTS = Constants()


class Elf(CharacterRace):
    def __init__(self):
        super().__init__("Elf", 35, CONSTANTS.WISDOM, CONSTANTS.DEXTERITY)


class Human(CharacterRace):
    def __init__(self):
        super().__init__("Human", 30, CONSTANTS.DEXTERITY, CONSTANTS.CHARISMA)
