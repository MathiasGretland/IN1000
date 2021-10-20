#Tom liste som lagrer alle tallene brukeren taster inn
liste = []
tall = int(input("Tast inn et tall: "))

#Så lenge tallet ikke er 0 vil den kjøre i en evig loop
while tall != 0:
    liste.append(tall)
    print(tall)
    tall = int(input("Tast inn et tall: "))

#Skriver ut alle tallene i listen på en pen måte
for i in range(len(liste)):
    print(liste[i])

#Adderer sammen alle tallene i listen og skriver ut en sluttsum
minSum = 0

for tall in liste:
    minSum += tall

print("Summen av tallene er:",minSum)

#Finner det minste tallet i listen
minste = liste[0]
for i in liste:
    if i < minste:
        minste = i

print("Her er det minste tallet:", minste)

#Finner det største tallet i listen
stoerst = liste[0]
for i in range(len(liste)):
    if liste[i] > stoerst:
        stoerst = liste[i]

print("Her er det største tallet:",stoerst)
