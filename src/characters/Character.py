from src.characterClass.ProtagonistClasses import *
from src.races.AntagonistRaces import *
from src.races.ProtagonistRaces import *
from src.characters.Stats import *
from src.items.Inventory import *
from src.items.weapons.Weapons import *
import random

random.seed()


class Character:
    def __init__(self, cr: CharacterRace, cc: CharacterClass, st: Stats):
        self._characterRace = cr
        self._characterClass = cc
        self._stats = st
        self._stats.statBonus1(self._characterRace.getStatBonus1())
        self._stats.statBonus2(self._characterRace.getStatBonus2())
        self._stats.setHealthArmor(self._characterClass.getHealth(), self._characterClass.getBaseArmor())
        self._inventory = Inventory([])

    def printCharacter(self):
        self._characterRace.printRace()
        self._characterClass.printClass()
        self._stats.printStats()
        self._inventory.printInventory()

    def getInventory(self):
        return self._inventory


testing = Character(Elf(), Monk(), Stats(1, 1, 1, 1, 1, 1))
testing.printCharacter()
print(testing.getInventory().getItem(0).__eq__(NullItem()))
testing.getInventory().addItem(Weapons("Short Sword", 8, "Slashing", 0, "Strength", "None"))
testing.getInventory().printInventory()
print(testing.getInventory().getItem(0).getDamage())
testing.getInventory().addItem(NullItem())
print(testing.getInventory().getItem(2).getDamage())
testing.getInventory().printInventory()
