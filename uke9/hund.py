class Hund:
    def __init__(self, alder, rase):
        self._alder = alder
        self._rase = rase

    def hentRase(self):
        return self._rase

    def settAlder(self, alder):
        self._alder = alder

    def hentAlder(self):
        return self._alder

print(Hund(10, "Puddel").hentRase())
print(Hund(12, "Labrador").hentAlder())

litenValp = Hund(4, "Chihuahua")

litenValp.settAlder(10)
storValp = litenValp

storValp.settAlder(12)

print(litenValp.hentAlder())

litenValp = Hund(2, "Labrador")

print(storValp.hentRase())
