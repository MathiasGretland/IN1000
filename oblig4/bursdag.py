"""
I denne oppgaven skal jeg lage et program som gjør at brukeren skal kunne få
en oversikt over dens venners bursdag, men brukeren skal også kunne oppdatere denne listen om personen har lyst
"""
#Printer ut en velkomst melding
print("Velkommen! her finner du en oversikt over dinne venners bursdager.")
print("")

#Orbok med noen navn og bursdager som man også kan gjøre om på
ordbok = {"Anders":"24/01", "Grete":"26/05", "Carl":"06/07", "Oskar":"01/12"}

#Velger å bruke et tall system for å kunne navigere seg i programmet
tall = 0

#Bruker while slik at programmet kan kjøre så lenge brukeren vil
while tall != 3:
    tall = int(input("Tast 1 for oversikt. Tast 2 for å legge til person. Tast 3 for å avslutte. "))
    #Printer ut oversikten
    if tall == 1:
        print("")
        print(ordbok)
        print("")
    #Gjør at man kan legge til en ny person
    elif tall == 2:
        nokkel = input("Navnet på denne personen? ")
        innhold = input("Når har denne personen bursdag? (f.eks 23/02) ")
        ordbok[nokkel] = innhold
        print("")
    #Gir feil melding hvis man kommer borti en knapp som er høyere enn 3
    elif tall > 3:
        print("Ugyldig input!")
        print("")
