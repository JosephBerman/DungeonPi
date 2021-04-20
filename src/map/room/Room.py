from src.map.room.Wall import *
from src.Constants import *
from src.characters.Character import *
from src.items.Item import *
from src.map.room.Wall import Wall

CONSTANT = Constants()


class Room:
    def __init__(self):
        self._north = None
        self._east = None
        self._south = None
        self._west = None
        self._player = None
        self._characters = []
        self._items = []

    def makeWalls(self, nt: Wall, et: Wall, st: Wall, wt: Wall):
        self._north = nt
        self._east = et
        self._south = st
        self._west = wt

    def addPlayer(self, pl: Character):
        self._player = pl

    def removePlayer(self):
        self._player = None

    def getPlayer(self) -> Character:
        return self._player

    def addCharacters(self, ch: Character):
        self._characters.append(ch)

    def addItem(self, it: Item):
        self._items.append(it)

    def movePlayer(self, dr: str):
        if dr == CONSTANT.NORTH:
            if type(self._north) is Door:
                self._north.getPath().addPlayer(self._player)
                self.removePlayer()
            elif type(self._north) is LockedDoor:
                if not self._north.isLocked():
                    self._north.getPath().addPlayer(self._player)
                    self.removePlayer()
        elif dr == CONSTANT.EAST:
            if type(self._east) is Door:
                self._east.getPath().addPlayer(self._player)
                self.removePlayer()
            elif type(self._east) is LockedDoor:
                if not self._east.isLocked():
                    self._east.getPath().addPlayer(self._player)
                    self.removePlayer()
        elif dr == CONSTANT.SOUTH:
            if type(self._south) is Door:
                self._south.getPath().addPlayer(self._player)
                self.removePlayer()
            elif type(self._south) is LockedDoor:
                if not self._south.isLocked():
                    self._south.getPath().addPlayer(self._player)
                    self.removePlayer()
        elif dr == CONSTANT.WEST:
            if type(self._west) is Door:
                self._west.getPath().addPlayer(self._player)
                self.removePlayer()
            elif type(self._west) is LockedDoor:
                if not self._west.isLocked():
                    self._west.getPath().addPlayer(self._player)
                    self.removePlayer()


room1 = Room()
room2 = Room()

room1.makeWalls(Door(room2), Wall(), Wall(), Wall())
room2.makeWalls(Wall(), Wall(), Door(room1), Wall())

testing = Character(Elf(), Monk(), Stats(1, 1, 1, 1, 1, 1))
room1.addPlayer(testing)
room1.getPlayer().printCharacter()
room1.movePlayer(CONSTANT.NORTH)
room2.getPlayer().printCharacter()
room2.movePlayer(CONSTANT.SOUTH)
room1.getPlayer().printCharacter()
