from src.map.room.Wall import *
from src.Constants import *

CONSTANT = Constants()


class Room:
    def __init__(self, nt: Wall, et: Wall, st: Wall, wt: Wall):
        self._north = nt
        self._east = et
        self._south = st
        self._west = wt
