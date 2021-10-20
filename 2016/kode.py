#Oppgave 1.1 20
#Oppgave 1.2
a = 10
b = 1
i = b
while i<a:
    b = b+i
    i=i+2
print(b)
#Oppgave 1.3 for i in range(5,10) vil svaret være = 56789.
#Oppgave 2.1 2
#Oppgave 2.2 Marit og Ole
#Oppgave 4.1
def median(a,b,c):
    if (a > b and a < c) or (a < b and a > c):
        return a
    elif (b > a and b < c) or ( b < a and b > c):
        return b
    return c

#Oppgave 5.1
def heltallsListe(heltall):
    nyListe = []
    for i in heltall:
        nyListe.append(i)
        nyListe.append(0)
    return nyListe

#Oppgave 6.1
def lesFraFil(filnavn):
    totUtgift = 0
    fil = open(filnavn)
    for line in fil:
        utgiftPerson = int(line)
        totUtgift += utgiftPerson
    return totUtgift

fn_peter = "Peter.txt"
tot_peter = lesFraFil(fn_peter)
print("Peter har brukt: ", tot_peter)

fn_paul = "Paul.txt"
tot_paul = lesFraFil(fn_peter)
print("Paul har brukt: ", tot_paul)

#Oppgave 7
class Gave:
    def __init__(self, navn, pris):
        self._navn = navn
        self._pris = pris

    def hentGavepris(self):
        return self._pris

    def hentNavn(self):
        return self._navn

    def __str__(self):
        return self._navn + "" + str(self._pris) + " kr"

#Oppgave 7.2
class Barn:
    def __init__(self, navn):
        self._navn = navn
        self._totalVerdi = 0
        self._gaver = []

    def hentNavn(self):
        return self._navn

    def totalVerdi(self):
        return self._totalVerdi

    def apneGave(self, nyGave):
        self._totalVerdi += nyGave.hentGavepris()
        self._gaver.append(nyGave)

    def skrivBarn(self):
        print(self._navn + ":")
        for gave in self._gaver:
            print(gave)
        print("Total veriden:" + self._totalVerdi)

#Oppgave 7.3
class Julekalender:
    def __init__(self, navnBarn, filnavn):
        self._apnere = []
        for navn in navnBarn:
            self._apnere.append(Barn(navn))

        self._kalender = []
        self._nesteApnere = 0
        self._dag = 0

        self._lesGavefil(filnavn)

    def nyDag(self, navn):
        if self._dag > 23:
            print("Alle gavene er åpnet!")
            return

        apner = self._apnere[self._nesteApnere]
        apner.apneGave(self._kalender[self._dag])
        self._dag += 1
        self._nesteApnere += 1

        if self._nesteApnere >= len(self._apnere):
            self._nesteApnere = 0

    def gaveOversikt(self):
        for apner in self._apnere:
            apner.skrivBarn()

    def _lesGavefil(self, filnavn):
        fil = open(filnavn)
        for linje in fil:
            biter = linje.split(",")
            gave = Gave(biter[0], float(biter[1]))
            self._kalender.append(gave)

#Oppgave 7.4
    self._hitorikk = {}
    self._lestHistorikk("Historikk.txt")

    def _lestHistorikk(self, histfilnavn):
        file = open(histfilnavn)
        for linje in file:
            linje = linje.split()
            navn = linje[0]
            self._historikk[navn] = []
            for gavenavn in words [1:]:
                self._historikk[navn].append(gavenavn)

#Oppgave 7.5
    def avergetLike(self):
        gaveFraDag = self._dag
        barnNavn = self._apnere[self._nesteApnere]

        while gaveFraDag < 24:
            gaveNavn = self._kalender[gaveFraDag]

            if gaveNavn not in self._historikk[barnNavn]:
                midlertidig = self._kalender[self._dag]
                self._kalender[self._dag] = self._kalender[gaveFraDag]
                self._kalender[gaveFraDag] = midlertidig
                return
            gaveFraDag += 1
        return False

#Oppgave 8.1
def bestehus(terninger):
    femmere = 0
    sekesere = 0
    for i in terninger:
        if i == 5:
            femmere += 1
        elif i == 6:
            seksere += 1
    return seksere == 3 and femmere == 2

#Oppgave 8.2
def hus(terninger):
    kast = [0,0,0,0,0,0]
    for i in t:
        kast[i-1] += 1

    if 2 in kast and 3 in kast:
        return True
    return False
