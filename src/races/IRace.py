import abc
import inspect

class IRace(abc.ABC):


    @abc.abstractmethod
    def printRace(self):
        pass

    @abc.abstractmethod
    def getName(self):
        pass

    @abc.abstractmethod
    def getSpeed(self):
        pass

    @abc.abstractmethod
    def getStatBonus1(self):
        pass

    @abc.abstractmethod
    def getStatBonus2(self):
        pass