class CharacterClass:
    def __init__(self, nm: str, ht: int, ba: int):
        self._name = nm
        self._health = ht
        self._baseArmor = ba

    def printClass(self):
        print(self._name, self._health, self._baseArmor)

    def getName(self):
        return self._name

    def getHealth(self):
        return self._health

    def getBaseArmor(self):
        return self._baseArmor
