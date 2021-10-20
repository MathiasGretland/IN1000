class Hamster:
    def __init__(self, n, v, k):
        self.navn = n
        self.vekt = v
        self.kjonn = k
        
        self.over = None
        self.under = None
        self.venstre = None
        self.hoyre = None
    
    def __eq__(self, hamster):
        if (self.navn == hamster.navn and self.kjonn == hamster.kjonn):
            return True
        else:
            return False
    
    def __str__(self):
        tekst = ""
        tekst += "\nNavn: " + self.navn
        tekst += "\nVekt: " + self.vekt
        tekst += "\nKjonn: " + self.kjonn
        return tekst
    