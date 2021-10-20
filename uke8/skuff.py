class Skuff:
    def __init__(self):
        self._mineSokker = []

    def settInnSokk(self, sokken):
        self._mineSokker.append(sokken)

    def sjekkStatus(self):
        antallVenstre = 0
        antallHoyre = 0

        for sokken in self._mineSokker:
            if(sokken.hentSide().lower() == "venstre"):
                antallVenstre += 1

            if(sokken.hentSide().lower() == "hoyre"):
                antallHoyre += 1

        if(antallHoyre == antallVenstre):
            print("Alt i orden")
        else:
            print("Ulik antall høyre og venstre sokker")
