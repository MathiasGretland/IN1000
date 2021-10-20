class Bok:
    def __init__(self, navn, forfatter,aar):
        self._navn = navn
        self._forfatter = forfatter
        self._aar = aar

    def hentNavn(self):
        return self._navn

    def hentAar(self):
        return self._aar

    def printBok(self):
        print("Navnet på boken:", self._navn, "Forfatteren:", self._forfatter, "Utgivelsesår:", self._aar)

    def erFirkanter(firkantListe):
        for firkant in firkantListe:
            if(not firkant.erFirkant()):
                return False
        return True
