from hamster import Hamster

class Hylle:
    def __init__(self, rad, kol):
        self.rader = rad
        self.kolonner = kol
        self.hamstere = []

        for r in range(0, self.rader):
            self.hamstere.append([])
            for k in range(0, self.kolonner):
                self.hamstere[r].append(None)

    def les_inn_fra_fil(self, filnavn):
        r = 0
        k = 0

        fil = open(filnavn)

        for linje in fil:
            biter = linje.split(", ")

            hamster = Hamster(biter[0], biter[1], biter[2])

            self.hamstere[r][k] = hamster

            k += 1

            if k == len(self.hamstere[0]):
                k = 0
                r += 1


    def print_alle_hamstere(self):
        for hylle in self.hamstere:
            for hamster in hylle:
                print(hamster.hent_info(), end="")

    def finn_duplikater(self):
        for r1 in range(0, self.rader):
            for k1 in range(0, self.kolonner):
                denne = self.hamstere[r1][k1]

                for r2 in range(0, self.rader):
                    for k2 in range(0, self.kolonner):
                        annen = self.hamstere[r2][k2]

                        if denne == annen:
                            if not (r1 == r2 and k1 == k2):
                                return True

        return False

    def __str__(self):
        tekst = ""
        for hylle in self.hamstere:
            for hamster in hylle:
                tekst += "|" + hamster.navn
            tekst += "|\n"
        return tekst

    def legg_til_naboer(self):
        for r in range(0, self.rader):
            for k in range(0, self.kolonner):
                hamster = self.hamstere[r][k]
                print()
                print(self)
                print("Denne:", hamster)

                if r > 0:
                    hamster.over = self.hamstere[r-1][k]
                    print("Over:", hamster.over)
                if r < len(self.hamstere) - 1:
                    hamster.under = self.hamstere[r+1][k]
                    print("Under:", hamster.under)
                if k > 0:
                    hamster.venstre = self.hamstere[r][k-1]
                    print("Venstre:", hamster.venstre)
                if k < len(self.hamstere) - 1:
                    hamster.hoyre = self.hamstere[r][k+1]
                    print("Hoyre:", hamster.hoyre)
