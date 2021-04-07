from src.combat.Damage import *

class Item:
    def __init__(self, nm: str):
        self._name = nm

    def __eq__(self, other):
        return self._name == other._name

    def returnItem(self):
        return self

    def printItem(self):
        return self._name

    def getDamage(self):
        return 0


class NullItem(Item):
    def __init__(self):
        super().__init__("NULL")

