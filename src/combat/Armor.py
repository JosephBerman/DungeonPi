from src.combat.Damage import *
from src.characters.Stats import *

class Armor:
    def __init__(self, st: Stats):
        self._armor = st.getArmor()
        self._health = st.getHealth()
