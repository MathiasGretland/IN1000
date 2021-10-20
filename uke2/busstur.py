sum = 0

inp = input("Stasjon 1! Hvor mange går på bussen?")
sum+= int(inp)

inp = input("Stasjon 2! Hvor mange går på bussen?")
sum+= int(inp)

inp = input("Stasjon 3! Hvor mange går på bussen?")
sum+= int(inp)

if sum < 30:
    print("Bussen kan kjøre")
else:
    print("Bussen er full. ", sum-30, "må gå til fots")

#Dette er riktig, men er ingen måte å sjekke hvor mange som er på bussen.
#Men det står i oppgaven at alle passasjerene skal til endestasjon.
