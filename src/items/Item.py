class Item:
    def __init__(self, nm: str):
        self._name = nm

    def returnItem(self):
        return self

    def printItem(self):
        return self._name
