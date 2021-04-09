from src.combat.Damage import *
from src.characters.Stats import *
from src.Constants import *

CONSTANT = Constants()

class Defence:
    def __init__(self, st: Stats):
        self._stats = st

    def defend(self, at: int, dm: int) -> int:
        if at == CONSTANT.CRITICAL:
            print("CRIT")
            self._stats.takeDamage(dm*2)
            return CONSTANT.HIT
        elif at >= self._stats.getArmor():
            print("HIT")
            self._stats.takeDamage(dm)
            return CONSTANT.HIT
        else:
            print("MISS")
            return CONSTANT.FAIL

