liste = ["en","to","tre"]

teller = 0
while teller < len(liste):
    print("indeks", teller, ":", liste[teller])
    teller += 1

tekst = input("Skriv noe fantastisk: ")
liste.append(tekst)

print(liste)
