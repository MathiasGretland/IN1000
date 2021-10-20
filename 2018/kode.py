#Oppgave 3a
"""
def penger(femkroninger, kronestykker):
    femkroninger = femkroninger * 5
    return femkroninger + kronestykker

print(penger(2,3))
"""

#Oppgave 3b
"""
def barnMedVoksen(alder1,alder2):
    if alder1 >= 18 and alder2 < 18:
        return True
    elif alder2 >= 18 and alder1 < 18:
        return True
    else:
        return False
"""

#Oppgave 3c

#Oppgave 3d

def fyllTilTi(tallene):
    """
    nyliste = []
    for tall in tallene:
        if not tall in nyliste:
            nyliste.append(tall)

    while len(nyliste) != 10:
        nyliste.append(0)

    return nyliste
    """
    """
    while len(tallene) != 10:
        tallene.append(0)
    return tallene
print(fyllTilTi([10,20,13,2]))
"""
#Oppgave 3e
"""
class Node :
    def __init__ (self, verdi) :
        self._verdi = verdi
        self._neste = None

    def settInn (self, ny) :
        self._neste = ny


    def skrivMeg (self) :
        print (self._verdi + "\n")
        if self._neste != None :
            self._neste.skrivMeg()


listeStart = Node("a")
ny = Node ("b")
listeStart.settInn(ny)
listeStart.skrivMeg()
print ("--------")
"""
#Oppgave 3f
"""
ny = Node ("c")
ny.settInn(listeStart)
listeStart = ny
listeStart.skrivMeg()
"""
#Oppgave 4a
class Hytte:
    def __init__(self, navn, antallSenger, prisForOvernatting):
        self._navn = navn
        self._antallSenger = antallSenger
        self._prisForOvernatting = prisForOvernatting

    def hentNavn(self):
        return self._navn

    def totPris(self, antall):
        return self._prisForOvernatting * antall

    def sjekkPlass(self, personer):
        return personer <= self._antallSenger

    def __str__(self):
        tekst = ""
        tekst += "Hyttas navn: " + self._navn + "\n"
        tekst += "Antall senger: " + str(self._antallSenger) + "\n"
        tekst += "Pris per natt: " + str(self._prisForOvernatting)
        return tekst

    def __eq__(self,annen):
        return self._navn == annen.hentNavn()

class Tur:
    def __init__(self, hytteliste, beskrivelse):
        self._hytteliste = hytteliste
        self._beskrivelse = beskrivelse

    def skrivTur(self):
        print(self._beskrivelse)
        for hytte in self._hytteliste:
            print(hytte)    # her kalles __str__ metoden i Hytte-klassen

    def sjekkPrisPlass(self, personer, maksbelop):
        for hytter in self._hytteliste:
            if self._antallSenger <= personer and self._prisForOvernatting <= maksbelop:
                return True
            else:
                return False

hytte = Hytte("KEKW", 5, 2000)
print(hytte)
print(hytte.sjekkPlass(6))

print(dank.sjekkPrisPlass(4,1500))
