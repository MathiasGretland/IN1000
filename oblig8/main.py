#Henter inn klassen Spillebrett fra filen spillebrett.py.
from spillebrett import Spillebrett

#Metode som kjører programmet basert på inputs fra brukeren.
def main():
    rader = int(input("Hvor mange rader vil du ha? "))
    kolonner = int(input("Hvor mange kolonner vil du ha? "))

    #Opretter et Spillebrett basert på dimensjonene til brukeren
    start = Spillebrett(rader, kolonner)

    #Tegner den nulte generasjon for cellesimuleringen.
    start.tegnBrett()

    #En string
    tekst = ""

    #While løkke som sier at så lenge stringen ikke er "q" så vil den kjøre.
    while tekst != "q":
        print()
        #Printer ut generasjonsnummer og kjører metoden finnAntallLevende
        print("Generasjonsnummer: ",start.generasjonsnummer, "-", "Antall levende celler:", start.finnAntallLevende())
        #Ber brukeren om input
        tekst = input("Trykk enter for å fortsette. Skriv inn q og trykk enter for å avslutte:")

        #Hvis brukeren kun taster inn ENTER, vil metoden oppdatering og tegnBrett kjøre
        if tekst == "":
            start.oppdatering()
            start.tegnBrett()


#Kjører metoden main.
main()
