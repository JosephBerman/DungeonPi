from src.items.Item import Item


class NullItem(Item):
    def __init__(self):
        super().__init__("NULL")

    def printItem(self):
        return self._name
