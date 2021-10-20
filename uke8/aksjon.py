class Vare:
    def __init__(self, beskrivelse):
        self._beskrivelse = beskrivelse
        self._hoyesteBud = None

    def by(self, pris):
        if self._hoyesteBud is None or self._hoyesteBud < pris:
            self._hoyesteBud = pris

    def seBud(self):
        if self._hoyesteBud is None:
            print("Ingen har lagt inn noe bud enda")
            return 0
        return self._hoyesteBud

klovn = Vare("Klovn")

klovn.by(12000)
print(klovn.seBud())
