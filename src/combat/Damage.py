from src.Constants import *

import random

random.seed()
CONSTANT = Constants()

class Damage:
    def __init__(self, dd: int, dt: str, mg: str):
        self._damageDie = dd
        self._damageType = dt
        self._magic = Magic(mg)

    def getDamage(self) -> int:
        if self._damageDie == 0:
            return 0
        else:
            return random.randint(1, self._damageDie) + self._magic.magicDamage()

    def getEffect(self):
        return self._magic.magicEffect()

    def getDamageType(self) -> str:
        return self._damageType



class Magic:
    def __init__(self, mg: str):
        self._magic = mg

    def magicDamage(self) -> int:
        if self._magic == CONSTANT.FIRE:
            return random.randint(1, 6)
        elif self._magic == CONSTANT.ICE:
            return random.randint(1, 4)
        else:
            return 0

    def magicEffect(self) -> str:
        if self._magic == CONSTANT.FIRE:
            return "Burned"
        elif self._magic == CONSTANT.ICE:
            return "Frozen"
        else:
            return "None"
