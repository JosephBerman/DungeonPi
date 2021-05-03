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

    # generateMap: None -> Map
    # generates a map for the player to explore
    def generateMap(self):
        origin = [(int(self._xcord / 2)), self._ycord - 1]
        print(origin)
        self.generateMapRooms(CONSTANT.ORIGIN, CONSTANT.ROOMRATE, origin)

    # generateMapRooms: String, Integer, List of Integers -> Room
    # Recursively generates rooms and connects them together, starting at the origin
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
            while True:
                direction = self.generateMapRoomsDirections(random.randint(0, 3))
                newCords = self.generateMapsNewCords(direction, cords)
                print(newCords)
                if self.generateMapRoomsEdgeCheck(direction, cords) and direction is not CONSTANT.SOUTH:
                    print("test")
                    break
            self.addRoom(Room(), newCords[1], newCords[0])
            if self.newRate(rate):
                self.generateMapRooms(direction, rate - 50, newCords)

        elif dir == CONSTANT.NONE:
            return

    # generateMapRoomsEdgeCheck : String, List of Integers
    # Checks to see if a room is able to be placed at the cords
    def generateMapRoomsEdgeCheck(self, dir: str, cords: list):
        if (cords[1] >= self._ycord) and (dir == CONSTANT.SOUTH):  # Highest Y
            return True
        elif (cords[1] <= 0) and (dir == CONSTANT.NORTH):  # Lowest Y
            return True
        elif (cords[0] >= self._xcord) and (dir == CONSTANT.EAST):  # Highest X
            return True
        elif (cords[0] <= 0) and (dir == CONSTANT.WEST):  # Lowest X
            return True
        elif type(self._level[cords[1]][cords[0]]) is not EmptyRoom:  # If a room already exists
            return True
        else:
            return False

    # generateMapRoomsDirection : Integer -> String
    # Random;y picks a new direction
    def generateMapRoomsDirections(self, num: int) -> str:
        if num == 0:
            print("North")
            return CONSTANT.NORTH
        elif num == 1:
            print("East")
            return CONSTANT.EAST
        elif num == 2:
            print("South")
            return CONSTANT.SOUTH
        elif num == 3:
            print("West")
            return CONSTANT.WEST

    # generateMapsNewCords : String, List of Integers -> List of Integers
    # generates a new cord dependant on what direction it was passed
    def generateMapsNewCords(self, dir: str, cords: list) -> list:
        if dir == CONSTANT.NORTH:
            return [cords[0], cords[1] - 1]
        elif dir == CONSTANT.SOUTH:
            return [cords[0], cords[1] + 1]
        elif dir == CONSTANT.WEST:
            return [cords[0] - 1, cords[1]]
        elif dir == CONSTANT.EAST:
            return [cords[0] + 1, cords[1]]
        else:
            return cords

    # newRate : Integer -> Boolean
    # Decides to generate more rooms or not
    def newRate(self, rt: int) -> bool:
        if random.randint(0, rt) == 0:
            return False
        return True

    #Prints the map
    def printMap(self):
        for i in range(self._ycord):
            print(self._level[i])

    #Adds a room
    def addRoom(self, rm: Room, x: int, y: int):
        self._level[x][y] = rm


testing = Map(3, 3)
test = Room()
testing.generateMap()
testing.printMap()
