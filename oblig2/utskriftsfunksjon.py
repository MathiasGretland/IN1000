"""
Her er et program som kommuniserer med brukeren slik at det tar inn et navn og
et bosted fra terminalen. Så skrives den ut 3 ganger.
"""

#Lager en prosedyre som inneholder fakta om personen
def personen():
    #Variabelen husker på navnet til brukeren
    navn = input("Skriv inn navn: ")
    #Variabelen husker på bostedet til brukeren
    bosted = input("Hvor kommer du fra? ")
    #Printer ut text, samt. inneholdet til variablene
    print(f'Hei, {navn}! Du er fra {bosted}')

#Prosedyre for å få et linjeskifte som ser penere ut
def linjeskift():
    print()

#Her blir prosedyrene satt i bruk
#Plasseringen avgjør hvilken rekkefølge prossedyrene skal kjøres i
personen()
linjeskift()
personen()
linjeskift()
personen()
