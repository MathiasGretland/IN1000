#Tom liste hvor byene lagres
steder = []
#for løkke som ber brukeren skrive inn 5 byer
for i in range(5):
    tekst = input("Skriv in en by: ")
    steder.append(tekst)

print(steder)

#Tomme lister for klessplagg og avreisedatoer
klesplagg = []
avreisedatoer = []

#for løkke som ber brukeren skrive inn 5 datoer og plagg
for i in range(5):
    dato = input("Skriv inn en dato (f.eks 27/03): ")
    plagg = input("Skriv inn et plagg du skal ha med: ")
    klesplagg.append(plagg)
    avreisedatoer.append(dato)

print("Her er avreisedatoene: ", avreisedatoer)
print("Her er klesplaggene du skal ha med: ", klesplagg)

print("*****")

#Slår alle listene sammen til en liste
reiseplan = [steder, klesplagg, avreisedatoer]

#Enkel for løkke som skriver ut innholdet i reiseplan
for i in reiseplan:
    print(i)

#Gjør at brukeren kan oppgi
i1 = input("Oppgi en plassering: ")
i2 = input("Oppgi en plassering: ")
i1 = int(i1)
i2 = int(i2)

#If setning som gjør plasseringen blir riktig, samt. hvis brukeren oppgir en Ugyldigplassering så vil den si ifra
if i1 <= 3 and i2 <= 5:
    print(reiseplan[i1-1][i2-1])
else:
    print("Ugyldig input!")
