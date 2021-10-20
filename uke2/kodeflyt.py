#Prisen er fastsatt til 50kr
pris = 50
#Ber brukeren om å skrive inn alderen sin
tekst = input("Skriv inn alder: ")
#Lager tekst variabelen om til en heltallsvariabel med navn alder
alder = int(tekst)

#Hvis alderen er 12 eller mindre, men og 67 eller mer. Så vil personen få halv pris
if alder < 12 or alder > 67:
    print("Du må betale", pris*0.5, "kr")
#Hvis alderen er mellom 12 og 67 må personen betale 50 kr
else:
    print("Du må betale", pris, "kr")
