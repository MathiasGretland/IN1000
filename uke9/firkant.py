from side import Side

class Firkant:
    def __init__(self):
        self._venstre = None
        self._hoyre = None
        self._topp = None
        self._bunn = None

    def leggTilSide(self, side ,plass):
        if (plass == "topp"):
            self._topp = side
        if (plass == "bunn"):
            self._bunn = side
        if (plass == "hoyre"):
            self._hoyre = side
        if (plass == "venstre"):
            self._venstre = side

    def fjernSide(self, plass):
        if(plass == "topp"):
            self._venste = None
        if(plass == "bunn"):
            self._bunn = None
        if(plass == "venstre"):
            self._topp = None
        if(plass == "hoyre"):
            self._hoyre = None

    def erFirkant(self):
        return self._venstre is not None and self._hoyre is not None and self._bunn is not None and self._topp is not None

bunn = Side(24,"blaa")
topp = Side(24,"blaa")
venstre = Side(24,"blaa")
hoyre = Side(24,"blaa")

firkanten = Firkant()
print(firkanten.erFirkant())
firkanten.leggTilSide(bunn,"bunn")
print(firkanten.erFirkant())
firkanten.leggTilSide(topp, "topp")
firkanten.leggTilSide(venstre, "venstre")
firkanten.leggTilSide(hoyre, "hoyre")
print(firkanten.erFirkant())

firkantListe = [firkanten]

print(erFirkanter(firkantListe))
