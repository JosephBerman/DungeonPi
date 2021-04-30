from src.map.room.Room import *
from src.map.room.Wall import *
from src.Constants import *
import random

random.seed()
CONSTANT = Constants()


class Map:
    def __init__(self, wd: int, ln: int):
        self._xcord = wd
        self._ycord = ln
        self._level = [[EmptyRoom() for i in range(self._xcord)] for j in range(self._ycord)]

    def generateMap(self):
        origin = [(int(self._xcord / 2)), self._ycord - 1]
        print(origin[0])
        print(origin[1])
        self.generateMapRooms(CONSTANT.ORIGIN, CONSTANT.ROOMRATE, origin)

    def generateMapRooms(self, dir: str, rate: int, cords: list):
        if dir == CONSTANT.NORTH:
            return
        elif dir == CONSTANT.EAST:
            return
        elif dir == CONSTANT.WEST:
            return
        elif dir == CONSTANT.SOUTH:
            return
        elif dir == CONSTANT.ORIGIN:
            self.addRoom(Room(), cords[1], cords[0])

        elif dir == CONSTANT.NONE:
            return

    def generateMapRoomsEdgeCheck(self, dir: str, cords: list):
        if (cords[1] == self._ycord) and (dir == CONSTANT.SOUTH):  # Highest Y
           return True
        elif (cords[1] == 0) and (dir == CONSTANT.NORTH):  # Lowest Y
            return True
        elif (cords[0] == self._xcord) and (dir == CONSTANT.EAST):  # Highest X
            return True
        elif (cords[0] == 0) and (dir == CONSTANT.WEST):  # Lowest X
            return True
        else:
           return False


    def printMap(self):
        for i in range(self._ycord):
            print(self._level[i])

    def addRoom(self, rm: Room, x: int, y: int):
        self._level[x][y] = rm


testing = Map(3, 2)
test = Room()
testing.generateMap()
testing.printMap()
