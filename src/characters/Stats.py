class Stats:
    def __init__(self, st: int, dx: int, cn: int, il: int, ws: int, ca: int):
        self._stre = st
        self._dex = dx
        self._con = cn
        self._intel = il
        self._wis = ws
        self._cha = ca
        self._health = None
        self._armor = None

    def printStats(self):
        print("str:", self._stre, "dex:", self._dex,
              "con:", self._con, "int:", self._intel, "wis:", self._wis,
              "cha:", self._cha, "Health:", self._health, "AC:", self._armor)

    def getStre(self):
        return self._stre

    def getDex(self):
        return self._dex

    def getCon(self):
        return self._con

    def getIntel(self):
        return self._intel

    def getWis(self):
        return self._wis

    def getCha(self):
        return self._cha

    def setHealthArmor(self, hh: int, ac: int):
        self._health = hh
        self._armor = ac

    def statBonus1(self, bn: str):
        if bn == "Strength":
            self._stre += 2
        elif bn == "Dexterity":
            self._dex += 2
        elif bn == "Constitution":
            self._con += 2
        elif bn == "Intelligence":
            self._intel += 2
        elif bn == "Wisdom":
            self._wis += 2
        elif bn == "Charisma":
            self._cha += 2

    def statBonus2(self, bn: str):
        if bn == "Strength":
            self._stre += 1
        elif bn == "Dexterity":
            self._dex += 1
        elif bn == "Constitution":
            self._con += 1
        elif bn == "Intelligence":
            self._intel += 1
        elif bn == "Wisdom":
            self._wis += 1
        elif bn == "Charisma":
            self._cha += 1