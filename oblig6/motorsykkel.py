#Opretter klassen Motorsykkel
class Motorsykkel:
    #Lager konstruktøren med instansvariablene som jeg trenger
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._kilometerstand = kilometerstand

    #Øker kilometerstanden
    def kjor(self, km):
        self._kilometerstand += km

    #Henter kilometerstanden
    def hentKilometerstand(self):
        return self._kilometerstand

    #Skriver ut merke, registreringsnummer og kilometerstand på en ryddig og fin måte
    def skrivUt(self):
        print("Merke:",self._merke,"\nRegistreringsnummer:",self._registreringsnummer,"\nKilometerstand:",self._kilometerstand)
