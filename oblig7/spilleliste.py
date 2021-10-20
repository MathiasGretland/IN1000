#Henter inn klassen Sang fra filen sang.py
from sang import Sang

#Oppretter klassen Spilleliste
class Spilleliste:
    #Lager konstruktøren med instansvariablene som jeg trenger
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    #En metode som først leser inn data fra en fil, denne leser inn data som sanger. Ved bruk av .split(';') splitter den artist fra tittel når et semikolon oppstår.
    #Etterhvert som filen leses oppretter den nye sanger til spillelisen ved bruk av .append()
    def lesFraFil(self, filnavn):
        fildata = open(filnavn)
        for linje in fildata:
            alleData = linje.strip().split(';')
            self._sanger.append(Sang(alleData[1],alleData[0]))
        fildata.close()

    #Legger til en sang til listen
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    #Metode som først sjekker om sangen finnes i listen, hvis dette er True fjerner den sangen.
    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.remove(sang)

    #Metode som spiller en sang
    def spillSang(self, sang):
        sang.spill()

    #Metode som spiller alle sangene i listen
    def spillAlle(self):
        for linje in self._sanger:
            linje.spill()
    #Metode som går igjennom listen etter den oppgitte tittelen, hvis dette finnes i listen, returnerer den tittelen. Hvis ikke returnerer den None
    def finnSang(self, tittel):
        for ord in self._sanger:
            if ord.sjekkTittel(tittel):
                return ord
        return None

    #Metode som henter ut sanger av en spesifikk artist
    #Først opretter jeg en ny liste, så sjekker jeg at hvis denne artisten som man oppgir finnes i den opprinnelige listen. Tar man sangene til denne artisten og .append() inn i den nye listen.
    #Så returneres den nye listen til slutt.
    def hentArtistUtvalg(self, artistnavn):
        self.liste = []
        for ord in self._sanger:
            if ord.sjekkArtist(artistnavn):
                self.liste.append(ord)
        return self.liste
