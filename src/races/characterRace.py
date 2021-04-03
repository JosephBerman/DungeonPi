class characterRace:
    def __init__(self, nm: str, sd: int, s1: str, s2: str):
        self.__name = nm
        self.__speed = sd
        self.__statBonus1 = s1
        self.__statBonus2 = s2

        super().__init__()

    def printRace(self):
        print(self.__name, self.__speed, self.__statBonus1, self.__statBonus2)

    def getName(self):
        return self.__name

    def getSpeed(self):
        return self.__speed

    def getStatBonus1(self):
        return self.__statBonus1

    def getStatBonus2(self):
        return self.__statBonus2
