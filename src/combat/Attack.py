from src.combat.Damage import *
from src.characters.Stats import *
from src.items.weapons.Weapons import *

class Attack:
    def __init__(self, st: Stats, wp: Weapons):
        self._stats = st
        self._weapons = wp
