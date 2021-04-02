from IRace import IRace


class raceElf(IRace):
    def __init__(self):
        self.__name = "Elf"
        self.__speed = 35
        self.__statBonus1 = "Wisdom"
        self.__statBonus2 = "Dexterity"
        pass

    def printRace(self):
        print(self.__name, self.__speed, self.__statBonus1, self.__statBonus2)

elf = raceElf()
elf.printRace()
