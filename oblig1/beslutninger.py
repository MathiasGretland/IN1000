#Her opprettes variabelen brus, ved hjelp av input kan brukeren selv velge hvilken verdi denne variabelen skal ha
brus = input("Har du lyst på en brus? ")

#Her kommer det noen if-setninger som utfører en handling utifra hva brukeren har skrevet inn.
#Hvis brukeren skriver "ja" skriver den ut "Her har du en brus!"
if brus == "ja":
    print("Her har du en brus!")
#Hvis brukeren skriver "nei" skriver den ut "Den er grei."
elif brus == "nei":
    print("Den er grei.")
#Hvis brukeren hverken skriver "ja" eller "nei" skriver den ut "Det forstod jeg ikke helt."
else:
    print("Det forstod jeg ikke helt.")
