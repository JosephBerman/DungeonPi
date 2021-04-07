from src.items.Item import *
from src.combat.Damage import *
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
        self._damage = Damage(self._damageDie, self._damageType, self._magic)


    def __eq__(self, other) -> bool:
        return (self._name == other._name and self._damageDie == other._damageDie and
                self._damageType == other._damageType and self._range == other._range and self._magic == other._magic)

    def printItem(self):
        print(self._name, self._damageDie, self._damageType, self._range, self._magic)

    def getDamage(self):
        return self._damage.getDamage()

    def getDamageDie(self):
        return self._damageDie

    def getDamageType(self):
        return self._damageType

    def getRange(self):
        return self._range

    def getMagic(self):
        return self._magic

