"""
I denne oppgaven har jeg lagd en liten quiz, poenget med denne quizen er å
gjette hovdestadene til forskjellige land. Den husker hvor mange man klarer, og
helt til slutt skriver den ut hvor mange hovedstader man kunne.
"""
#Printer ut en hyggelig velkomst beskjed
print("Hei! Velkommen til hovedstads-quizen!")

#Dette er en global variabel som holder på antall hovedstader brukeren husker
sum = 0

#Dette er en prosedyre for spørsmål 1
def spoorsmaal1():
    #Spør brukeren om å skrive inn hovedstaden i England
    svar = input("Hva heter hovedstaden i England?\n> ")
    #Svaret på spørsmålet
    riktig_svar = "London"

    #Hvis svaret er riktig kjører denne
    if svar == riktig_svar:
        #Må bruke global for å kunne bruke den globale variabelen sum
        global sum
        #Plusser på 1 hvis svaret er riktig
        sum+= 1
        #Skriver ut "korrekt"
        print("Korrekt!")
    #Hvis svaret er feil kjører denne
    else:
        #Skriver ut "Feil svar"
        print("Feil svar.")

#Dette er en prosedyre for spørsmål 2
def spoorsmaal2():
    #Spør brukeren om å skrive inn hovedstaden i Frankrike
    svar = input("Hva heter hovedstaden i Frankrike?\n> ")
    #Svaret på spørsmålet
    riktig_svar = "Paris"

    #Hvis svaret er riktig
    if svar == riktig_svar:
        #Må bruke global for å kunne bruke den globale variabelen sum
        global sum
        #Plusser på 1 hvis svaret er riktig
        sum+= 1
        #Skriver ut "korrekt"
        print("Korrekt!")
    #Hvis svaret er feil kjører denne
    else:
        #Skriver ut "Feil svar"
        print("Feil svar.")

#Dette er en prosedyre for spørsmål 3
def spoorsmaal3():
    #Spør brukeren om å skrive inn hovedstaden i Latvia
    svar = input("Hva heter hovedstaden i Latvia?\n> ")
    #Svar på spørsmålet
    riktig_svar = "Riga"

    #Hvis svaret er riktig
    if svar == riktig_svar:
        #Må bruke global for å kunne bruke den globale variabelen sum
        global sum
        #Plusser på 1 hvis svaret er riktig
        sum+= 1
        #Skriver ut "korrekt"
        print("Korrekt!")
    #Hvis svaret er feil kjører denne
    else:
        #Skriver ut "Feil svar"
        print("Feil svar.")

#Her blir prosedyrene (spørsmålene) satt i bruk
#Plasseringen avgjør hvilken rekkefølge prossedyrene skal kjøres i
spoorsmaal1()
spoorsmaal2()
spoorsmaal3()

#Skriver ut hvor mange riktige brukeren klarte
print("Du kunne ", sum, " av 3 hovedstader.")
