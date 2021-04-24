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
        self._player = Character
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
        self._player = EmptyCharacter()


    def getPlayer(self) -> Character:
        return self._player

    def addCharacters(self, ch: Character):
        self._characters.append(ch)

    def addItem(self, it: Item):
        self._items.append(it)

    def movePlayer(self, dr: str):
        if dr == CONSTANT.NORTH:
            self.movePlayerDir(self._north)
        elif dr == CONSTANT.EAST:
            self.movePlayerDir(self._east)
        elif dr == CONSTANT.SOUTH:
            self.movePlayerDir(self._south)
        elif dr == CONSTANT.WEST:
            self.movePlayerDir(self._west)

    def movePlayerDir(self, wl: Wall):
        if type(wl) is Door:
            wl.getPath().addPlayer(self._player)
            self.removePlayer()
        elif type(wl) is LockedDoor:
            if not wl.isLocked():
                wl.getPath().addPlayer(self._player)
                self.removePlayer()
            else:
                print("Door Locked")



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
room2.getPlayer().printCharacter()