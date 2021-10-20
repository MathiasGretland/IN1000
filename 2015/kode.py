#Oppgave 1
#a) 12
#b) -4 -8
#Oppgave 2
#a) 2
#b) 6
#Oppgave 4
"""
def beregnAreal(lengde, bredde):
    if lengde < 0 or bredde < 0:
        return -1
    return lengde * bredde
"""
#Oppgave 5 AB210
#Oppgave 6
"""
def kampResultat(scoringerLagA, scoringerLagB):
    if scoringerLagA > scoringerLagB:
        return "hjemme"
    elif scoringerLagA < scoringerLagB:
        return "borte"
    return "uavgjort"
"""
#Oppgave 7 a og b
class Attraksjon:
    def __init__(self, navn, barn, fra, til):
        self._navn = navn
        self._barn = barn
        self._fra = fra
        self._til = til

    def skrivAttr(self):
        utskrift = self._navn + ". " + str(self._fra) + " - " + str(self._til)
        if self._barn:
            utskrift = "BARN" + utskrift
        else:
            utskrift = "VOKSEN" + utskrift
        print(utskrift)

    def forBarn(self):
        return self._barn


    def aapenIPeriode(self, fra, til):
        if fra > self._til or til < self._fra:
            return False
        return True

#Oppgave 7 c, d og e
class Destinasjon:
    def __init__(self, navn, attraksjoner):
        self._navn = navn
        self._attraksjoner = attraksjoner

    def hentDestNavn(self):
        return self._navn

    def skrivDest(self):
        print("Destinasjon:" + self._navn)
        for a in self._attraksjoner:
            a.skrivAttr()

    def leggTilAttr(self, nyAttr):
        self._attraksjoner.append(nyAttr)

    def antallAktuelleAttr(self, barn, fraDato, tilDato):
        total = 0
        for a in self._attraksjoner:
            if(not barn or a.forBarn()) and a.aapenIPeriode(fraDato, tilDato):
                total += 1
        return total

#Oppgave 7 f, g, h og i(vanskelig) #finnBesteDest
class Katalog:
    def __init__(self, katalogfil):
        self._katalogfil = katalogfil
        self._destKatalog = {}
        self.lesDestinasjonsfil(self._katalogfil)

    def _lesDestinasjonsfil(self, filnavn):
        pass

    def skrivDestListe(self):
        print("Destinasjoner:")
        for d in self._destKatalog:
            print(d)

    def skrivEnDest(self, destNavn):
        if destNavn in self._destKatalog:
            self._destKatalog[destNavn].skrivDest()
        else:
            print("Ingen destinasjoner med navnet", destNavn)

    def nyAttr(self, destNavn, attrNavn, bVennlig, apenFra, apenTil):
        if destNavn in self._destKatalog:
            nyAttr = Attraksjon(attrNavn, bVennlig, apenFra, apenTil)
            self._destKatalog[destNavn].leggTilAttr(nyAttr)

    def nyDestFraFil(self, destNavn, filnavn):
        if destNavn not in self._destKatalog:
            self._destKatalog[destNavn] = Destinasjon(destNavn, [])

        fil = open(filnavn)

        attrNavn = fil.readline().rstrip()
        while attrNavn != "":
            hvem = fil.readline().rstrip()
            if hvem == "VOKSNE":
                forBarn = False
            else:
                forBarn = True
            fraDato = int(fil.readline().rstrip())
            tilDato = int(fil.readline().rstrip())
            self.nyAttr(destnavn, attrNavn, forBarn, fraDato, tilDato)
            attrNavn = fil.readline().rstrip()

    def finnBesteDest(self, barn, fra, til):
        besteDest = ""
        besteAntall = 0

        for destNavn in self._destKatalog:
            dest = self._destKatalog[destNavn]
            antall = dest.antallAktuelleAttr(barn, fra, til)
            if antall > besteAntall:
                bestDest = destNavn
                besteAntall = antall
        return besteDest

#Oppgave 9
#a)
def trimZeros(a):
    forsteIndeks = 0
    while forsteIndeks < len(a) and a[forsteIndeks] == 0:
        forsteIndeks += 1

    sisteIndeks = len(a) - 1
    while sisteIndeks >= 0 and a[sisteIndeks] == 0:
        sisteIndeks -= 1

    return a[forsteIndeks:sisteIndeks + 1]

#b)
def antallBokstaver(tekst):
    liste = []
    for a in tekst:
        if a not in liste:
            liste.append(a)
    return len(liste)

v = antallBokstaver("accag")
