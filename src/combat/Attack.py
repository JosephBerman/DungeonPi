from src.combat.Damage import *
from src.characters.Stats import *
from src.items.weapons.Weapons import *
from src.Constants import *
import random

random.seed()
CONSTANTS = Constants()

class Attack:
    def __init__(self, st: Stats, wp: Weapons):
        self._stats = st
        self._weapons = wp

#TODO figure out how i want to handle taking the hit
    def getAttack(self) -> int:
        roll = random.randint(1, CONSTANT.D20)
        if roll == 20:
            print("Critical Hit!")
            return self._weapons.getDamage()  * 2 + self._weapons.getBonus(self._stats)
        elif roll == 1:
            print("Critical Miss!")
            if random.randint(1, CONSTANT.D4) == 1:
                print("You hurt yourself for", random.randint(1, CONSTANT.D4))

            return 0
        else:
            return roll + self._weapons.getBonus(self._stats)
