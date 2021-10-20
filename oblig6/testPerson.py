#from/import blir brukt for å kunne hente klassen man lagde i en fil, for å bruke den i et ny fil
from person import Person

navn = input("Skriv inn navnet ditt: ")
alder = input("Skriv inn alderen din: ")

#Tar informasjonen til brukeren og lager en objekt ut av informasjon
bruker = Person(navn, alder)

print("Tast h for å legge til en hobby. Tast a for å avslutte")

#While løkke som kjører så lenge tekst ikke er "a"
tekst = ""
while tekst != "a":
    tekst = input("Skriv en kommando (h eller a)")
    if tekst == "h":
        bruker.leggTilHobby()

#Skriver ut informasjonen
bruker.skrivUt()
