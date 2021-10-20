from random import randint

class Stasjon:
    def __init__(self, navn):
        self._navn = navn
        self._naboer = []

    def sett_nabo(self, nabo):
        self._naboer.append(nabo)

    def hent_navn(self):
        return self._navn

    def hent_tilfeldig_nabo(self):
        tilfeldig_tall = randint(0, len(self._naboer)-1)
        return self._naboer[tilfeldig_tall]


def hovedprogram():
    stasjonsfil = open("ruter_full.txt")

    stasjonsbok = {}
    for linje in stasjonsfil:
        biter = linje.strip().split()
        fra_stasjon_navn = biter[0]
        til_stasjon_navn = biter[1]

        if fra_stasjon_navn not in stasjonsbok:
            stasjonsbok[fra_stasjon_navn] = Stasjon(fra_stasjon_navn)
        fra_stasjon = stasjonsbok[fra_stasjon_navn]

        if til_stasjon_navn not in stasjonsbok:
            stasjonsbok[til_stasjon_navn] = Stasjon(til_stasjon_navn)
        til_stasjon = stasjonsbok[til_stasjon_navn]

        fra_stasjon.sett_nabo(til_stasjon)
        til_stasjon.sett_nabo(fra_stasjon)



    start_navn = input("Hvor vil du reise fra?")
    maal_navn = input("Hvor vil du reise til?")

    sted = stasjonsbok[start_navn]
    while maal_navn != sted.hent_navn():
        sted = sted.hent_tilfeldig_nabo()
        print(sted.hent_navn())

    print("Du er fremme!")

hovedprogram()
