#Oppretter klassen Hund
class Hund:
    #Lager konstruktøren med instansvariablene som jeg trenger
    def __init__(self, alder, vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    #Henter alderen
    def hentAlder(self):
        return self._alder

    #Henter vekten
    def hentVekt(self):
        return self._vekt

    #Får hunden til å springe
    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    #Får hunden til å spise
    def spis(self, heltall):
        self._metthet += heltall
        if self._metthet > 7:
            self._vekt += 1
