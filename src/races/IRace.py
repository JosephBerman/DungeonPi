import abc

class IRace(abc.ABC):

    @abc.abstractmethod
    def printRace(self):
        pass

    __name: str
    __speed: int
    __statBonus1: str
    __statBonus2: str
