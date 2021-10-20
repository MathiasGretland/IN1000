#Lager ordboken med navn varer
varer = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print(varer)

#Ber brukeren om å skrive inn en ny vare, samt. prisen
nyVare = input("Skriv inn en ny vare: ")
nyPris = float(input("Prisen til denne varen? "))
#Får varen + prisen inn i den eksisterende orboken varer
varer[nyVare] = nyPris

#Ber brukeren om å skrive inn enda en ny vare, samt. prisen
nyVare = input("Skriv inn enda en ny vare: ")
nyPris = float(input("Prisen til denne varen? "))
#Får varen + prisen inn i den eksisterende orboken varer
varer[nyVare] = nyPris

print(varer)
