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

    # TODO figure out how i want to handle taking the hit
    def getAttack(self, item: Item) -> int:
        roll = random.randint(1, CONSTANT.D20)
        if type(item) is not Weapons:
            return CONSTANT.ITEMATTACK
        if roll == 20:
            print("Critical Hit!")
            return CONSTANT.CRITICAL
        elif roll == 1:
            print("Critical Miss!")
            return CONSTANT.FAIL
        else:
            return roll + item.getBonus(self._stats)

