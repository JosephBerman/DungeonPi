from src.items.Item import *

class Key(Item):
    def __init__(self, nm: str, id: int):
        super().__init__(nm)
        self._ID = id

    def getID(self):
        return self._ID

    def setID(self, id: int):
        self._ID = id