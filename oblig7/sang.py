#Oppretter klassen Sang
class Sang:
    #Lager konstruktøren med instansvariablene som jeg trenger
    def __init__(self, artist, tittel):
        self._tittel = tittel
        self._artist = artist

    #Spiller av sangen i terminalen
    def spill(self):
        print("Spiller:", self._tittel, "av artisten:", self._artist)

    #Sjekker om artisten som er skrevet inn matcher med artisten som blir laget med klassen
    def sjekkArtist(self, navn):
        navn = navn.lower()
        self._artist = self._artist.lower()
        for ord in self._artist.split():    #For hvert ord i artist navnet som splitter for hver spacebar, altså " "
          if ord in navn:           #Hvis da ordet er i det nye navnet som er oppgit:
              return True
        return False

    #Sjekker om tittelen som er skrevet inn matcher med tittelen som blir laget i klassen
    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        return False

    #Sjekker om artist og tittel matcher med det som blir laget i klassen
    #Valgte å få de til å kjøre via de andre metodene som jeg lagde i oppgaven for å gjøre det på den enklest mulige måten
    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkArtist(artist) is True and self.sjekkTittel(tittel) is True:
            return True
        return False
