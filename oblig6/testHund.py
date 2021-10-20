#from/import blir brukt for å kunne hente klassen man lagde i en fil, for å bruke den i et ny fil
from hund import Hund

#hovedprogram som utfører handlinger
def hovedprogram():
    hund1 = Hund(4, 10)

    hund1.spring()
    print(hund1.hentVekt())
    hund1.spring()
    print(hund1.hentVekt())
    hund1.spring()
    print(hund1.hentVekt())
    hund1.spring()
    print(hund1.hentVekt())
    hund1.spis(3)
    print(hund1.hentVekt())
    hund1.spring()
    print(hund1.hentVekt())
    hund1.spring()
    print(hund1.hentVekt())
    hund1.spring()
    print(hund1.hentVekt())
    hund1.spring()
    print(hund1.hentVekt())
    hund1.spis(5)
    print(hund1.hentVekt())
    hund1.spis(5)
    print(hund1.hentVekt())

#Kjører programmet
hovedprogram()
