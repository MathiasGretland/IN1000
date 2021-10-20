
#Når man leser inn fra en fil og skal legge elementene inn i en liste som ser slik ut:
#Karl Marx, 2914
def _lesGavefil(self, filnavn):
    fil = open(filnavn)
    for linje in fil:
        biter = linje.split(",")
        gave = Gave(biter[0], float(biter[1]))
        self._kalender.append(gave)

#Når man leser inn fra en fil og skal legge elemente inn i en dict
def hentBesvarelser(self, filnavn):
    besvarelser = {}
    fil = open(filnavn)
    for linje in fil:
        biter = linje.split()
        brukernavn = biter[0]
        besvarelse = biter[1]
        besvarelser[brukernavn] = besvarelse
    return besvarelser

#Denne gjør at man kan legge til flere elementer som nøkkelverdi i en dict. Her er det tatt utgangspunkt i at metoden er lagd i en klasse. En fil vil da kanskje se slik ut: barnenavn gavenavn gavenavn gavenavn gavenavn
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


#Fullt hus yatzy eksempel
def bestehus(terninger):
    femmere = 0
    sekesere = 0
    for i in terninger:
        if i == 5:
            femmere += 1
        elif i == 6:
            seksere += 1
    return seksere == 3 and femmere == 2

#Sjekker om det er hus yatzy eksempel
def hus(terninger):
    kast = [0,0,0,0,0,0]
    for i in t:
        kast[i-1] += 1

    if 2 in kast and 3 in kast:
        return True
    return False


#Viser hvordan man går igjennom en ordbok, og finner det laget med høyest poengsum.
def gull(lagoversikt):
    beste_lag = None
    maks_poeng = 0
    for lag in lagoversikt:
        poeng = lagoversikt[lag]
        if poeng>maks_poeng:
            beste_lag = lag
            maks_poeng = poeng
    return beste_lag

assert gull({"Brann" : 2, "Molde" : 3}) == "Molde"
assert gull({"Brann" : 4, "Molde" : 3}) == "Brann"

#Fyord oppgaven fra Prøveeksamen
def sjekk_om_fyord(setning, fyord, synonym_liste):
    biter = setning.split()
    for bit in biter:
        for synonym in synonym_liste:
            if bit in synonym and fyord in synonym:
                return True
    return fyord in biter

#Oppgave 5 Prøveeksamen 2018
#a)
def ring(i, v):
    while v[i] != -1:
        i = v[i]
    return i

assert ring(1, [2, -1, -1, 0])==1
assert ring(3, [2, -1, -1, 0]) == 2


#b)
def gyldig(v):
    for start in range(len(v)):
        i = start
        teller = 0
        while v[i] != -1 and teller<len(v):
            teller +=1
            i = v[i]
            if i == start:
                return False
    return True

assert gyldig([2, -1, -1, 0])
assert not gyldig([1,-1, 3,4,2])
assert not gyldig([3, -1, -1, 4, 3])

def gyldig2(ansatte) :
    for i in range(len(ansatte)) :
        j = i
        sett = []
        while ansatte[j] != -1 :
            sett.append(j)
            j = ansatte[j]
            if j in sett :
                return False
    return True

assert gyldig2([2, -1, -1, 0])
assert not gyldig2([1,-1, 3,4,2])
assert not gyldig2([3, -1, -1, 4, 3])


#Sjekk ut 2019Prøveeksamen for restaurant, har klassene: Rett, kategori, meny, kunde og TakeAway. Står eksamen høsten 2018 i dokumentet
#Prøveeksamen i år og 2019H handler om å rette studenters obliger, har klassene: Emne, Student, Retter og oblig
#2016 har klassene: Gave, barn og Julekalender
#2015 har klassene: Attraksjon, Destinasjon og Katalog
#2017 har klassene: Bud, Annonse, kategori, bruktmarked
#2018 har klassene: hytter, tur og turplanlegger
