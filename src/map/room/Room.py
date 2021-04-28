from src.map.room.Wall import *
from src.Constants import *
from src.characters.Character import *
from src.items.Item import *
from src.map.room.Wall import Wall

CONSTANT = Constants()


class Room:
    def __init__(self):
        self._north = Wall()
        self._east = Wall()
        self._south = Wall()
        self._west = Wall()
        self._player = Character
        self._characters = []
        self._items = []

    def changeWall(self, dr, wl: Wall):
        if dr == CONSTANT.NORTH:
            self._north = wl
        elif dr == CONSTANT.EAST:
            self._east = wl
        elif dr == CONSTANT.SOUTH:
            self._south = wl
        elif dr == CONSTANT.WEST:
            self._west = wl

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

room1.changeWall(CONSTANT.NORTH, Door(room2))
room2.changeWall(CONSTANT.SOUTH, Door(room1))

testing = Character(Elf(), Monk(), Stats(1, 1, 1, 1, 1, 1))
room1.addPlayer(testing)
room1.getPlayer().printCharacter()
room1.movePlayer(CONSTANT.NORTH)

room2.getPlayer().printCharacter()
room2.movePlayer(CONSTANT.SOUTH)
room1.getPlayer().printCharacter()
