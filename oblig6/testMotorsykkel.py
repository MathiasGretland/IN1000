#from/import blir brukt for å kunne hente klassen man lagde i en fil, for å bruke den i et ny fil
from motorsykkel import Motorsykkel

#hovedprogram som utfører handlinger
def hovedprogram():
    sykkel1 = Motorsykkel("Harley Davidson", "AY23817", 138273)
    sykkel2 = Motorsykkel("Yamaha", "SU62738", 27263)
    sykkel3 = Motorsykkel("Suzuki", "AX83625", 23716)

    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()

    sykkel3.kjor(10)
    print(sykkel3.hentKilometerstand())

#Kjører programmet
hovedprogram()
