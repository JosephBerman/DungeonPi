from src.map.room.Room import *
from src.map.room.Wall import *
import random

random.seed()


class Map:
    def __init__(self, wd: int, ln: int):
        self._width = wd
        self._length = ln
        self._level = [[EmptyRoom() for i in range(self._width)] for j in range(self._length)]

    def generateMap(self):
        origin = [(int(self._width / 2)), self._length -1]
        print(origin[0])
        print(origin[1])
        self.addRoom(Room(), origin[1], origin[0])

    def printMap(self):
        for i in range(self._length):
            print(self._level[i])

    def addRoom(self, rm: Room, x: int, y: int):
        self._level[x][y] = rm


testing = Map(3, 2)
test = Room()
testing.generateMap()
testing.printMap()