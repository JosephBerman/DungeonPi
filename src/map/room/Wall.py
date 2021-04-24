from src.map.room.Room import *
from src.items.Key import *
from src.Constants import *

CONSTANT = Constants()


class Wall:
    def __init__(self):
        self._path = CONSTANT.WALL

    def getPath(self):
        return self._path


# TODO I need to fix this circle depdancy, thinking of making a connection class

class Door(Wall):
    def __init__(self, rm):
        super().__init__()
        self._path = rm


class LockedDoor(Door):
    def __init__(self, rm, ky: Key):
        super().__init__(rm)
        self._ID = ky.getID()
        self._locked = True

    def unlock(self, ky: Key):
        if self._ID == ky.getID():
            self._locked = False
            print("Unlocked")
        else:
            print("Locked, incorrect key")

    def isLocked(self):
        if self._locked:
            print("Door locked.\n")
        return self._locked

    def getPath(self):
        if self._locked:
            print("The door is locked")
            return CONSTANT.LOCKED
        else:
            return super()._path
