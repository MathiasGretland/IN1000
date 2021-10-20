#Oppgave 1
#a) 3
#b) ad
#c) 17
#d) 9
#e) 16
#f) 32

#Oppgave 2
#a) 49
#b) 60
#c) 49
#d) 49

#Oppgave 3
#a)
def vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal):
    if hjemmemaal > bortemaal:
        return hjemmelag
    elif hjemmemaal < bortemaal:
        return bortelag
    else:
        return "uavgjort"

#b)
def forkort_lagliste(lagliste):
    nyLagListe = []
    for i in lagliste:
        if i not in lagliste:
            nyLagListe.append(i)
    return nyLagListe

#c)
def legg_inn_null_maal(lagliste):
    dict = {}
    for i in lagliste:
        dict[i] = 0
    return dict

#d)
def ekstraher_lagliste(fn):
    nyListe = []
    fil = open(fn)
    for linje in fil:
        biter = linje.split()
        hjemmelag = biter[0]
        bortelag = biter[1]
        nyListe.append(hjemmelag)
        nyListe.append(bortelag)
    return nyListe

#e)
def regn_poengsum(fn):
    lagliste = ekstraher_lagliste(fn)
    lagoversikt = legg_inn_null_maal(lagliste)

    for linje in open(fn):
        biter = linje.split()
        hjemmelag = biter[0]
        bortelag = biter[1]
        hjemmemaal = int(biter[2])
        bortemaal = int(biter[3])
        vinneren = vinnerlag(hjemmelag, bortelag, hjemmemaal, bortemaal)
        if vinneren==hjemmelag:
            lagoversikt[hjemmelag] += 3
        elif vinneren==bortelag:
            lagoversikt[bortelag] += 3
        else: #Uavgjort
            lagoversikt[hjemmelag] += 1
            lagoversikt[bortelag] += 1
    return lagoversikt

#f)
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

#g)
def finn_gull(fn):
    lagoversikt = regn_poengsum(fn)
    vinnerlag = gull(lagoversikt)
    print(vinnerlag)
    assert vinnerlag == "brann"

#Oppgave 4
#a)
class Rett:
    def __init__(self, navn, pris, innholdsstoffer):
        self._navn = navn
        self._pris = pris
        self._innholdsstoffer = innholdsstoffer

    def sjekkInnholdOk(unngaa):
        for innh in self._innholdsstoffer:
            if innh in uungaa:
                return False
        return True

    def __str__(self):
        utskrift = "Navn: " + self._navn + "Pris: " + str(self._pris) + ". Innhold:"
        for i in self._innholdsstoffer:
            utskrift += " " + i
        return utskrift

#b)
class Kategori:
    def __init__(self, katNavn, retter):
        self._kNavn = katNavn
        self._retter = retter

    def hentOkRetter(self, innholdsstoffer):
        nyListe = []
        for i in self._retter:
            if i.sjekkInnholdOk(innholdsstoffer):
                nyListe.append(i)
        return nyListe

#c)
class Meny:
    def __init__(self, kategoriNavn):
        self._kategorier = {}
        for kategori in kategorinavn:
            nyKat = self._lesKategoriFil (knavn+".txt")
            self.kategorier[kategorier] = nyKat

    def hentRedusertMeny(self, unngaas):
        okKategorier = {}
        for i in self._kategorier:
            retter = self._kategorier[i].hentOkRetter(unngaas)
            if retter:
                nyKat = Kategori(i, retter)
                okKategorier[i] = nyKat
        return okKategorier

#d)
class Kunde:
    def __init__(self, telefon, innholdsstoffer):
        self._telefon = telefon
        self._innholdsstoffer = innholdsstoffer

    def velgRetter(self, meny):
        kategorier = meny.hentRedusertMeny(self._innholdsstoffer)
        bestilling = []
        for k in kategorier.values():
            k.skrivKategori()
            valg = input("Skriv inn ønsket rett med kommentarer, eller tom linje: ")
            if valg != "":
                bestilling.append(valg)
        return bestilling

#e)
class TakeAway :
	def __init__(self, kategorier, kundefilnavn):
		self._meny = Meny(kategorier)
		self._kundekatalog = self._lesKundefil(kundefilnavn)

	def betjenKunde (self, kundeTlf):
		kunde = self._kundekatalog[kundeTlf]
		bestilling = kunde.velgRetter(self._meny)
		self._lagOgLeverMat(bestilling)

	def _lagOgLeverMat(self, bestilling):
		print("Følgende er bestilt: ")
		for bestillingstekst in bestilling :
			print(bestillingstekst)

#f)
def hovedprogram():
	mineKategorier = ["Forretter", "Hovedretter", "Desserter"]
	minTakeAway = TakeAway(mineKategorier, "kunder.txt")
	kundeId = input("Oppgi telefonnr: ")
	while kundeId != "" :
		minTakeAway.betjenKunde(kundeId)
		kundeId = input("Oppgi telefonnr: ")

hovedprogram()
