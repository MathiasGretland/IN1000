#Oppgave 3a
"""
def hastighet(fart):
    if fart <= 60:
        return "fart:" + str(fart)
    else:
        return "fart:over 60"

print(hastighet(56))
print(hastighet(65))
"""

#Oppgave 3b
"""
def sjekkVerdier(tallene, min, max):
    for tall in tallene:
        if tall <= min or tall => max:
            return False
    return True
#Dersom min > max vil testen "tall <= min or tall => max" alltid være sant, så funksjonen vil alltid returnere False.
"""

#Oppgave 3c
"""
def hovedprogram():
    a = Node("a")
    a.settInnHoyre(Node("b"))
    a.settInnVenstre(Node("c"))

hovedprogram()
"""

#Oppgave 4

class Bud:
    def __init__(self, budgiver, budStr):
        self._budgiver = budgiver
        self._budStr = budStr
        if budStr <= 0:
            self._budStr = 1

    def hentBudgiver(self):
        return self._budgiver

    def hentBudStr(self):
        return self._budStr

class Annonse:
    def __init__(self, annTekst):
        self._annTekst = annTekst
        self._bud = []

    def hentTekst(self):
        return self._annTekst

    def giBud(self, hvem, belop):
        nyttBud = Bud(hvem, belop)
        self._bud.append(nyttBud)

    def antBud(self):
        return len(self._bud)

    def hoyesteBud(self):
        hoyeste = None
        hoyesteVerdi = 0
        for bud in self._bud:
            if bud.hendtBudStr() > hoyesteVerdi:
                hoyeste = bud
                hoyesteVerdi = bud.hendtBudStr()
        return hoyeste

    #Oppgave 4e
    def kraftBud(self, hvem, belop, max):
        budBelop = belop
        hoyeste = self.hoyesteBud().hendtBudStr()
        if belop < hoyeste:
            budBelop = hoyeste + 1
        if budBelop > max:
            budBelop = max
        self.giBud(hvem, budBelop)


class Kategori:
    def __init__(self, katNavn):
        self._katNavn = katNavn
        self._annonseListe = []

    def nyAnnonse(self, annTekst):
        ny = Annonse(annTekst)
        self._annonseListe.append(ny)
        return ny

    def hentAnnonser(self):
        return self._annonseListe

class Bruktmarked:
    def __init__(self):
        self._ordbok = {}

    def nyKategori(self, katNavn):
        if finnKategori(katnavn) == None:
            nyKat = Kategori(katnavn)
            self._ordbok[katNavn] = nyKat
            return nyKat
        else:
            return None

    def finnKategori(self, katNavn):
        for kat in self._ordbok:
            if kat == katNavn:
                return self._ordbok[kat]
        return None

def hovedprogram():
    bruktmarked = Bruktmarked()
    kategori = bruktmarked.nyKategori("sykkellykt")
    annonse = kategori.nyAnnonse("New Yorker sykkellykt")
    annonse.giBud("Peter", 42)
    annonse.giBud("Ann", 0)
    annonse.kraftBud("Mary", 40, 50)

    hoyesteBudStr = ann.hoyesteBud().hentBudStr()
    budGiver = ann.hoyesteBud().hentBudgiver()

    print(hoyesteBudStr, "gitt av", budGiver)
    #Alternativt med assert
    assert hoyesteBudStr == 43
    assert budGiver == "Mary"

hovedprogram()
