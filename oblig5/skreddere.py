"""
I denne oppgaven skal jeg lage et beregningsprogram for skreddere som har en funksjon som leser inn en fil med navn på mål og selve målet i tommer. Denne funksjonen legger denne informasjonen i en ordbok hvor navnet på målet er nøkkelverdien og returnerer ordboken. Deretter er det en prosedyre som tar imot ordboken og benytter seg av tommerTilCm funksjonen som jeg skrev i en annen oppgave
som skriver ut målene i cm.
"""

#Open blir brukt slik at når man kaller på variabeln fildata, så vil den bruke informasjonen som er i txt filen
fildata = open("skredderetext.txt")
navnOgMaal = {}
#Funksjon som lager en ordbok utfra innholdet i txt filen
def leseFraFil():
    for linje in fildata:
        biter = linje.split()
        navn = biter[0]
        maal = biter[1]
        navnOgMaal[navn] = maal
    return navnOgMaal

#Kjører funksjonen samt skriver ut en informativ tekst
print("Ordbok med navn og tommer", leseFraFil())

#Funksjon som jeg tok fra oppgave 1
def tommerTilCm(antallTommer):
    antallTommer = float(antallTommer)
    assert antallTommer > 0
    # Regner ut hvor mange tommer det er i cm
    antallTommer = antallTommer * 2.54
    return antallTommer

#Tekst for å gjøre programmet penere i terminalen
print("Her er målene gjort om til tommer:")

#Prosedyre som får tar alle mål verdiene og får de til å kjøre i funksjonen tommerTilCm
def printOrdbokICm():
    for i in navnOgMaal:
        print("Gjort om til cm",tommerTilCm(navnOgMaal[i]))

#Kjører funksjonen
printOrdbokICm()
