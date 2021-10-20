from espressomaskin import EspressoMaskin

kunde1 = EspressoMaskin(1000)

print(kunde1.lagLungo())
print(kunde1.lagEspresso())

kunde1.fyllVann(100)

print(kunde1.lagLungo())
