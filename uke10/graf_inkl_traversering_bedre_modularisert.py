from random import randint

class Stasjon:
    def __init__(self, navn):
        self._navn = navn.strip()
        self._naboer = []

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def hent_navn(self):
        return self._navn

    def hent_tilfeldig_nabo(self):
        indeks = randint(0, len(self._naboer)-1)
        return self._naboer[indeks]


def fordrukken_traversering(fra, til):
    lokasjon = fra
    while lokasjon != til:
        lokasjon = lokasjon.hent_tilfeldig_nabo()
        print(lokasjon.hent_navn())

def bygg_graf():
    stasjonsbok = {}
    for linje in open("ruter_full.txt"):
        biter = linje.strip().split()
        fra_navn = biter[0]
        if not fra_navn in stasjonsbok:
            stasjonsbok[fra_navn] = Stasjon(fra_navn)
        fra_stasjon = stasjonsbok[fra_navn]
        til_navn = biter[1]
        if not til_navn in stasjonsbok:
            stasjonsbok[til_navn] = Stasjon(til_navn)
        til_stasjon = stasjonsbok[til_navn]
        fra_stasjon.legg_til_nabo(til_stasjon)
        til_stasjon.legg_til_nabo(fra_stasjon)
    return stasjonsbok

def hovedprogram():
    stasjonsboka = bygg_graf()
    startsted = input("Hvor vil du reise fra?: ")
    start = stasjonsboka[startsted]
    maalsted = input("Hvor vil du reise til?")
    maal = stasjonsboka[maalsted]
    fordrukken_traversering(start, maal)

hovedprogram()
