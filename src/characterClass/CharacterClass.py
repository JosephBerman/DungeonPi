from src.Constants import *

CONSTANT = Constants()


class CharacterClass:
    def __init__(self, nm: str, ht: int, ba: int):
        self._name = nm
        self._baseHealth = ht
        self._baseArmor = ba

    def printClass(self):
        print(self._name, self._baseHealth, self._baseArmor)

    def getName(self):
        return self._name

    def getHealth(self):
        return self._baseHealth

    def getBaseArmor(self):
        return self._baseArmor


class EmptyClass(CharacterClass):
    def __init__(self):
        super().__init__(CONSTANT.NONE, 0, 0)
