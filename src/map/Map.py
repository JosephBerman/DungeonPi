from src.map.room.Room import *
from src.map.room.Wall import *


class Map:
    def __init__(self, wd: int, ln: int):
        self._width = wd
        self._length = ln
        self._level = [[EmptyRoom() for i in range(self._width)] for j in range(self._length)]

    def printMap(self):
        for i in range(self._length):
            print(self._level[i])


testing = Map(3,3)
testing.printMap()