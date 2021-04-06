from .weapons import *
from ..items.Item import *
from .NullItem import *


class Inventory:

    def __init__(self, ims: list):
        if ims is not None:
            self._items = ims
        else:
            self._items = [NullItem()]

    def printInventory(self):
        print(self._items)

    def getInventory(self):
        return self._items

    def addItem(self, itm):
        self._items.append(itm)

    def getItem(self, im: int):
        if len(self._items) == 0:
            return 0
        elif im >= len(self._items):
            return 0
        elif im < 0:
            return 0
        else:
            return self._items[0].returnItem()
