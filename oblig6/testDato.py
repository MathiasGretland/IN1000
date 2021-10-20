#from/import blir brukt for å kunne hente klassen man lagde i en fil, for å bruke den i et ny fil
from dato import Dato

#Opretter et nytt objekt
dato1 = Dato(15, 7, 1997)

#Skriver ut datoen til terminalen
print(dato1.lesAar())

#Skriver ut en melding siden dagen er den 15.
dato1.bestemtDag()

#Lagrer datoen som en streng
dato1.lagStreng()

#Printer tekststrengen med en tekst som passer til akkurat den datoen
print(dato1.lagStreng(), "Er datoen Gianni Versace ble skutt og drept i sin egen mansion i Miami")
