class CharacterRace:
    def __init__(self, nm: str, sd: int, s1: str, s2: str):

        self._name = nm
        self._speed = sd
        self._statBonus1 = s1
        self._statBonus2 = s2



    def printRace(self):
        print(self._name, self._speed, self._statBonus1, self._statBonus2)

    def getName(self):
        return self._name

    def getSpeed(self):
        return self._speed

    def getStatBonus1(self):
        return self._statBonus1

    def getStatBonus2(self):
        return self._statBonus2

