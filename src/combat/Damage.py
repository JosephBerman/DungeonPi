import random

random.seed()


class Damage:
    def __init__(self, dd: int, dt: str, mg: str):
        self._damageDie = dd
        self._damageType = dt
        self._magic = mg

    def getDamage(self) -> int:
        return random.randint(1, self._damageDie)

    def getMagicDamage(self):
        pass

    def getDamageType(self) -> str:
        return self._damageType
