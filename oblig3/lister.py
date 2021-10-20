#Variabel som definerer den første lista
liste = [4, 7, 9]
#Legger til et element i lista
liste.append(5)

#Printer de ut
print(liste[0])
print(liste[2])

#Ny tom liste
navneListe = []

#Skrives det inn navn som kommer til lista
navn = input("Skriv inn et navn: ")
navneListe.append(navn)
navn = input("Skriv inn et navn til: ")
navneListe.append(navn)
navn = input("Skriv inn enda et navn til: ")
navneListe.append(navn)
navn = input("Skriv inn et siste navn: ")
navneListe.append(navn)

#If setning som sier at hvis navnet mitt er der printer den at brukeren husket dette
#Hvis brukeren ikke husket navnet mitt spør den brukeren om jeg ble glemt
if "Mathias" in navneListe:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#Beregner summen og produktet
sum = liste[0] + liste[1] + liste[2] + liste[3]
produkt = liste[0] * liste[1] * liste[2] * liste[3]
#Legger inn i egen liste
RegneListe = [sum, produkt]

#Legger listene sammen til en liste
finalListe = [liste, RegneListe]
print(finalListe)

#Fjerner elementer
del finalListe[1][1]
del finalListe[1][0]
print(finalListe)
