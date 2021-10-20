class Bilde:
    def __init__(self, hoyde, bredde, salgspris):
        self._hoeyde = hoyde
        self._bredde = bredde
        self._salgspris = salgspris

    def hentForhold(self):
        sideforhold = self._bredde / self._hoeyde
        return sideforhold

    def hentSalgspris(self):
        return self._salgspris
#------------------------------------------------------

mittBilde = Bilde(10, 15, 20000)
print(mittBilde.hentForhold())

annetBilde = Bilde(160, 150, 10500)
annetBilde = Bilde(160, 150, 2000)
print(annetBilde.hentSalgspris())

monaLisa = Bilde(250, 150, 5000)
skrik = Bilde(400, 400, 1000)

print(skrik.hentForhold() + monaLisa.hentSalgspris())

rhein2 = Bilde(73, 143)
print(rhein2.hentSalgspris(2))

sisteBilde = Bilde("100", "200", 4000)
print(sisteBilde.hentForhold())

print(Bilde(200, 200, 4500).hentSalgspris())
