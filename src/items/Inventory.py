from src.items.weapons.Weapons import *


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

    def addItem(self, itm: Item):
        if self._items[0].__eq__(NullItem()):
            self._items[0] = itm
        else:
            self._items.append(itm)

    def getItem(self, im: int) -> Item:
        if len(self._items) == 0:
            return NullItem()
        elif im >= len(self._items):
            return NullItem()
        elif im < 0:
            return NullItem()
        else:
            return self._items[im].returnItem()

