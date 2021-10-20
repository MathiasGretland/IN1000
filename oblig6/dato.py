#Opretter klassen Dato
class Dato:
    #Lager konstruktøren med instansvariablene som jeg trenger
    def __init__(self, nyDag, nyMaaned, nyttAar):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyttAar = nyttAar
        self._dato = ""

    #Leser av året for datoen
    def lesAar(self):
        return self._nyttAar

    #Gjør datoen om til en tekststreng
    def lagStreng(self):
        self._dato = self._nyDag, self._nyMaaned, self._nyttAar
        return self._dato

    #Printer ut en gitt tekst om datoen er en bestemt dato på forhånd
    def bestemtDag(self):
        if self._nyDag == 15:
            print("Loenningsdag!")
        elif self._nyDag == 1:
            print("Ny maaned, nye muligheter")
