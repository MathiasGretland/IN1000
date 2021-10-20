class Rektangel:
    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde

    def oekLengde(self, oekning):
        self._lengde += oekning

    def oekBredde(self, oekning):
        self._bredde += oekning

    def areal(self):
        return (self._lengde * self._bredde)

    def omkrets(self):
        return (self._lengde * 2 + self._bredde * 2)

    def reduserLengde(self, reduksjon):
        self._lengde -= reduksjon

    def reduserBredde(self, reduksjon):
        self._bredde -= reduksjon

rektangel1 = Rektangel(5,10)
rektangel2 = Rektangel (22,52)

print(rektangel1.areal())
print(rektangel2.areal())

rektangel1.oekLengde(5)
rektangel2.oekBredde(6)

print(rektangel1.omkrets())
print(rektangel2.omkrets())
