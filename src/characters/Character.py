from src.characterClass.CharacterClass import *
from src.characterClass.ProtagonistClasses import *
from src.races.CharacterRace import *
from src.races.AntagonistRaces import *
from src.races.ProtagonistRaces import *
from src.characters.Stats import *
from src.items.Inventory import *
from src.items.weapons.Weapons import *
from src.combat.Attack import *
from src.combat.Defence import *
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
        self._attack = Attack(self._stats)
        self._defence = Defence(self._stats)

    def printCharacter(self):
        self._characterRace.printRace()
        self._characterClass.printClass()
        self._stats.printStats()
        self._inventory.printInventory()

    def getStats(self):
        return self._stats

    def getInventory(self):
        return self._inventory

    def getAttack(self):
        return self._attack

    def getDefence(self):
        return self._defence


class EmptyCharacter(Character):

    def __init__(self):
        super().__init__(EmptyRace(), EmptyClass(), Stats(0, 0, 0, 0, 0, 0))



testing = Character(Elf(), Monk(), Stats(1, 1, 1, 1, 1, 1))
testing.getInventory().addItem(Weapons("Short Sword", 6, CONSTANT.SLASHING, 0, CONSTANT.STRENGTH, CONSTANT.FIRE))

test = Character(Elf(), Wizard(), Stats(1, 1, 1, 1, 1, 1))
test.getInventory().addItem(Weapons("Short Sword", 6, CONSTANT.SLASHING, 0, CONSTANT.STRENGTH, CONSTANT.NONE))

test.getDefence().defend(testing.getAttack().getAttack(testing.getInventory().getItem(0)),
                         testing.getInventory().getItem(0).getDamage())

print(test.getStats().getCurrentHealth())
