min_liste = ["Oslo", "Bergen"]

#Hviser lengden (Hvor mange verdier variabelen har)
len(min_liste)

#Sjekker om en verdi finnes:
"Bergen" in min_liste #True
"Trondheim" in min_liste #False

#Telle
#Teller hvor mange 1945 verdier det er
liste = [1945, 1814, 1905, 1945]
print(liste.count(1945))

#Sortere
#Sorterer fra lavest til høyest
liste.sort()
print(liste) # [1814, 1905, 1945, 1945]

tekst = "kamel"
sorted(tekst) #"aeklm"
tekst.count("m") #1
"""
tekst.append("a") #en tekst streng er immutable, altså den kan ikke endres. aka dette fungerer ikke
"""
