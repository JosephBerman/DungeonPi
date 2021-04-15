from src.combat.Damage import *
from src.characters.Stats import *
from src.items.weapons.Weapons import *
from src.Constants import *
import random

random.seed()
CONSTANT = Constants()


class Attack:
    def __init__(self, st: Stats):
        self._stats = st

    def getAttack(self, item: Item) -> int:
        roll = random.randint(1, CONSTANT.D20)
        if type(item) is not Weapons:
            return CONSTANT.ITEMATTACK
        if roll == CONSTANT.CRITICALROLL:
            print("Critical Hit!")
            return CONSTANT.CRITICAL
        elif roll == CONSTANT.FAILROLL:
            print("Critical Miss!")
            return CONSTANT.FAIL
        else:
            return roll + item.getBonus(self._stats)

