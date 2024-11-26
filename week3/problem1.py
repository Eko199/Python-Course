from math import log2

class Player:
    def __init__(self, name, hp, xp):
        self._name = name
        self._hp = hp
        self._xp = xp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        self._hp = max(value, 0)

    @property
    def xp(self):
        return self._xp
    
    @xp.setter
    def xp(self, value):
        self._xp += value

    @property
    def level(self):
        return 1 if self.xp < 300 else 2 + log2(int(self.xp / 300))
    
player = Player("Axz", 100, 400)
player.xp = 400
print(player.level)