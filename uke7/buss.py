class Buss:
    def __init__(self, kapasitet):
        self._kapasitet = kapasitet
        self._antallPassasjerer = 0

    def hentAntall(self):
        print("Det er", self._antallPassasjerer, "på bussen")

    def erFull(self):
        return self._antallPassasjerer >= self._kapasitet

    def erTom(self):
        return self._antallPassasjerer == 0

    def plukkOpp(self):
        if self.erFull():
            print("Bussen er full")
        else:
            print("Velkommen om bord")
            self._antallPassasjerer += 1

    def slippAv(self):
        if self._erTom():
            print("Det er ingen passasjerer å slippe av")
        else:
            print("Takk for turen")
            selv._antallPassasjerer -= 1

def hovedprogram():
        bussen = Buss(20)
        for i in range(10):
            bussen.plukkOpp()
        bussen.hentAntall()
        for i in range(12):
            bussen.plukkOpp()
        bussen.hentAntall()

hovedprogram()
