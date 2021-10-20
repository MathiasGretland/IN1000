nye_ord = []
while len(nye_ord) < 5:
    nye_ord.append(input("Skriv inn ord! "))

print("***")

indeks = 0
while indeks<5:
    svar = input("Hva er ordet? ")
    if svar == nye_ord[indeks]:
        print("Riktig")
    else:
        print("Galt")
    indeks += 1
