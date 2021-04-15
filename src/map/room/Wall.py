from src.map.room.Room import *
from src.Constants import *

CONSTANT = Constants()


class Wall:
    def __init__(self):
        self._path = CONSTANT.WALL

    def getPath(self):
        return self._path


class Door(Wall):
    def __init__(self, rm: Room):
        super().__init__()
        self._path = rm

