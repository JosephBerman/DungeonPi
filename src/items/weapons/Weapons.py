from ..Item import *
import random

random.seed()


# TODO add parent class item to weapons and have the inventory take it
class Weapons(Item):
    def __init__(self, nm: str, dd: int, dt: str, rg: int, mg: str):
        super().__init__(nm)
        self._damageDie = dd
        self._damageType = dt
        self._range = rg
        self._magic = mg

    def printItem(self):
        print(self._name, self._damageDie, self._damageType, self._range, self._magic)

    def getDamageDie(self):
        return self._damageDie

    def getDamageType(self):
        return self._damageType

    def getRange(self):
        return self._range

    def getMagic(self):
        return self._magic

    # TODO Figure out what types of magic damage I want to have and create a damage class to handle status effects
    def magicBonus(self):
        if self._magic == "Fire":
            return random.randint(1, 4)
        elif self._magic == "Ice":
            return random.randint(1, 4)
        else:
            return 0
