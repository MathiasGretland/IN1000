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
        print("Navnet på boken: ", self._navn, "Forfatteren: ", self._forfatter, "Utgivelsesår: ", self._aar)

class Bokhylle:
    def __init__(self, maksplass):
        self._maksplass = maksplass
        self._listeBoker = []

    def leggTilBok(self, enBok):
        if len(self._listeBoker) < self._maksplass:
            self._listeBoker.append(enBok)
            return True
        return False

    def erDetPlass(self):
        if len(self._listeBoker) < self._maksplass:
            return True
        return False

    def finnBok(self, navn, aar):
        for bok in self._listeBoker:
            if (bok.hentNavn() == navn) and (bok.hentAar() == aar):
                return bok
        return False

    def printBokhylle(self):
        for boker in self._listeBoker:
            boker.printBok()


bokhylle = Bokhylle(7)
bok1 = Bok("Versace", "Harald", 1976)
bok2 = Bok("Swag", "Meg", 3005)
bokhylle.leggTilBok(bok1)
bokhylle.leggTilBok(bok2)
bokhylle.printBokhylle()
