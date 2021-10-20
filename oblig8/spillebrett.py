#Gjør at jeg kan bruke metoden randint fra random.
from random import randint
#Henter inn klassen Celle fra filen celle.py.
from celle import Celle

#Opretter klassen Spillebrett.
class Spillebrett:
    #Lager konstruktøren med instansvariablene som jeg trenger
    #Opretter en liste som fylles med Celle-objekter likt antall rader ganger antall kolonner.
    #Oppretter også variabelen generasjonsnummer som skal øke for 1 hver gang brettet oppdateres, men dette kommer mer tydelig fram i metoden oppdatering.
    def __init__(self, rader, kolonner):
        self.rader = rader
        self.kolonner = kolonner
        self.rutenett = []
        self.generasjonsnummer = 0

        for r in range(self.rader):
            self.rutenett.append([])
            for k in range(self.kolonner):
                self.rutenett[r].append(Celle())

        #Kjører metoden _generer i selve konstruktøren.
        self._generer()

    #Metoden går igjennom hele rutenettet og printer ut alle Celle-objektene en etter en.
    def tegnBrett(self):
        print("\n" * 30)
        for spillebrett in self.rutenett:
            print()
            for celle in spillebrett:
                print(celle.hentStatusTegn(), end="")

    #Metoden beregner neste generasjon av celler.
    def oppdatering(self):
        #Inneholder alle døde celler som skal få status "levende".
        self.dodeCeller = []
        #Inneholder alle levende celle som skal få status "død".
        self.levendeCeller = []

        #Går igjennom rutenett.
        for r in range(len(self.rutenett)):
            for k in range(len(self.rutenett[r])):
                #Sjekker naboene til Celle-objektet.
                naboer = self.finnNabo(r,k)

                #Lagrer naboene som er i live.
                self.levendeNaboer = []

                #Sjekker om nabocellene er levende, hvis de er det lagres de i levendeNaboer.
                for celler in naboer:
                    if celler.erLevende():
                        self.levendeNaboer.append(celler)

                #Returnerer statusen til hoved cellen.
                celleObjekt = self.rutenett[r][k]
                hovedCelle = celleObjekt.erLevende()

                #If setninger basert på om hovedcellen er i live eller ikke.
                if hovedCelle == True:
                    #Hvis den er i live vil den gå igjennom hvor mange levende naboer Celle-objektet har, og utifra disse if-setningene avgjøre om cellen skal leve eller død.
                    if len(self.levendeNaboer) < 2 or len(self.levendeNaboer) > 3:
                        self.levendeCeller.append(celleObjekt)

                    if len(self.levendeNaboer) == 3 or len(self.levendeNaboer) == 2:
                        self.dodeCeller.append(celleObjekt)

                else:
                    #Hvis den ikke er i live vil den gå igjennom hvor mange levende naboer Celle-objektet har, og hvis den har nøyaktig 3 levende naboer, vil den døde cellen bli satt til liv.
                    if len(self.levendeNaboer) == 3:
                        self.dodeCeller.append(celleObjekt)

        #Gjør at cellene i listen blir satt til død.
        for celle in self.levendeCeller:
            celle.settDoed()
        #Gjør at cellene i listen blir satt til levende.
        for celle in self.dodeCeller:
            celle.settLevende()
        #For hver gang denne metoden blir kjørt vil generasjonsnummer øke med 1.
        self.generasjonsnummer += 1

    #Metoden går igjennom alle Celle-objektene i rutenett, for hver levende celle så vil telleren øke. Så kan derfor enkelt bare returnere telleren for å finne ut hvor mange celler som er i live.
    def finnAntallLevende(self):
        teller = 0
        for r in self.rutenett:
            for k in r:
                if k.erLevende() is True:
                    teller += 1
        return teller

    #_generer sørger for at hvert eneste Celle-objekt har 1/3 sjanse for å få statusen "levende".
    def _generer(self):
        for r in range(0,self.rader):
            for k in range(0,self.kolonner):
                #randint gjør at vi enkelt kan returnere et tilfeldig tall mellom to tall. i dette eksempelet mellom 0 - 2, inkludert 0 og 2 selvsagt.
                random = randint(0,2)

                #Kunne også sagt blant annet sagt: if random == 0 eller noe lingnende. Er flere valgmuligheter her.
                if random < 1:
                    self.rutenett[r][k].settLevende()


    #finnNabo skal finne ut statusen til Celle-objektets naboer. Altså de cellene som er rundt.
    #rad og kolonne er kordinatene til det Celle-objektet som skal få sjekket naboene sine.
    def finnNabo(self, rad, kolonne):
        #Inneholder alle naboene til Celle-objektet.
        self.naboListe = []

        #Her skriver vi range(-1, 2) fordi vi er på utkikk etter å finne naboen til cellen. Derfor når rad + r og kolonne + k blir satt -1 på, finner vi cellene som er ved siden av og over og under.
        for r in range(-1,2):
            for k in range(-1,2):
                naboRad = rad + r
                naboKolonne = kolonne + k

                #Dette er for å forsikre seg om at nabo cellen faktisk eksisterer.
                gyldigNabo = True

                #Disse if-setningene er sier kort sagt at hvis naboen er gyldig så vil den bli lagt til i naboListe. Er den False vil den ikke det
                #Man kan ikke legge til det Celle-objektet som man skal finne naboene til
                if (naboRad) == rad and (naboKolonne) == kolonne:
                    gyldigNabo = False

                #Man kan ikke legge til et objekt som er utenfor radene. Altså et objekt som ikke eksisterer
                if (naboRad) < 0 or (naboRad) >= self.rader:
                    gyldigNabo = False

                #Man kan ikke legge til et objekt som er utenfor kolonnene. Altså et objekt som ikke eksisterer
                if (naboKolonne) < 0 or (naboKolonne) >= self.kolonner:
                    gyldigNabo = False

                #Hvis da naboen er gyldig vil den bli lagt til i naboListe
                if gyldigNabo:
                    self.naboListe.append(self.rutenett[naboRad][naboKolonne])

        #Returnerer listen med alle cellens naboer.
        return self.naboListe
