#Opretter klassen Celle.
class Celle:
    #Lager konstruktøren. Den gjør at for hver celle som blir oprettet så får de statusen "død".
    def __init__(self):
        self.status = "død"

    #Endre status. Setter statusen til "død".
    def settDoed(self):
        self.status = "død"

    #Endre status. Setter statusen til "levende".
    def settLevende(self):
        self.status = "levende"

    #Hente status. Returnerer True eller False avhengig om cellens status er "levende" eller "død".
    def erLevende(self):
        if self.status == "levende":
            return True
        return False

    #Hente status. Avhengig om cellen sin status er True eller False, vil den returnere "O" eller "."
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        return "."
