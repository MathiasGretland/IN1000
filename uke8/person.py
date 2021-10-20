class Person:

    def __init__(self, navn):
        self._navn = navn
        self._partner = None

    def bryllup(self, nyPartner):
        self._partner = nyPartner

    def minStatus(self):
        if self._partner:
            print("Beklager, jeg er alt gift med", self._partner.hentNavn())
        else:
            print("Jeg er på sjekker'n")

    def hentNavn(self):
        return self._navn
