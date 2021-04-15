from src.items.Item import *
from src.combat.Damage import *
from src.Constants import *
from src.characters.Stats import *

import random

random.seed()


class Weapons(Item):
    def __init__(self, nm: str, dd: int, dt: str, rg: int, bs: str, mg: str):
        super().__init__(nm)
        self._damageDie = dd
        self._damageType = dt
        self._range = rg
        self._bonus = bs
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

    def getBonus(self, st: Stats):
        if self._bonus == CONSTANT.STRENGTH:
            return st.getStre()
        elif self._bonus == CONSTANT.DEXTERITY:
            return st.getDex()
        elif self._bonus == CONSTANT.CONSTITUTION:
            return st.getCon()
        elif self._bonus == CONSTANT.INTELLIGENCE:
            return st.getIntel()
        elif self._bonus == CONSTANT.WISDOM:
            return st.getWis()
        elif self._bonus == CONSTANT.CHARISMA:
            return st.getCha()

    def getRange(self):
        return self._range

    def getMagic(self):
        return self._magic
