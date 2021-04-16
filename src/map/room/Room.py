from src.map.room.Wall import *
from src.Constants import *
from src.characters.Character import *
from src.items.Item import *

CONSTANT = Constants()


class Room:
    def __init__(self, nt: Wall, et: Wall, st: Wall, wt: Wall):
        self._north = nt
        self._east = et
        self._south = st
        self._west = wt
        self._player = None
        self._characters = []
        self._items = []

    def addPlayer(self, pl: Character):
        self._player = pl

    def removePlayer(self):
        self._player = None

    def addCharacters(self, ch: Character):
        self._characters.append(ch)

    def addItem(self, it: Item):
        self._items.append(it)
'''
    def movePlayer(self, dr: str):
        if dr == CONSTANT.NORTH:
            if self._north is type(Door):
                self._north.getPath().addPlayer(self._player)
                self.removePlayer()
            elif self._north is type(LockedDoor):
                if not self._north.isLocked():
                    self._north.getPath().addPlayer(self._player)
                    self.removePlayer()


'''



