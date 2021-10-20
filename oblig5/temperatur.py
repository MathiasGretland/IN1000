#Lager en funksjon som skal ta imot en fil og returnere en ordbok
def maxTempPerMaaned():
    maxTempPerMaanedFil = open("max_temperatures_per_month.csv")
    maxTempPerMaanedOrdbok = {}
    for linje in maxTempPerMaanedFil:
        #bruker .split(",") for å kunne splitte nøkkelverdier og innholdsverdier
        biter = linje.split(",")
        maaned = biter[0]
        temperatur = biter[1]
        #Legger inn i ordbok
        maxTempPerMaanedOrdbok[maaned] = float(temperatur)
    return maxTempPerMaanedOrdbok

print(maxTempPerMaaned())

#Lager en funksjon som setter de to orbøkene opp mot hverandre og gjør at den nye ordboken blir oppdatert med de høyeste temperaturene
def varmeRekord():
    maxTempPerMaanedDictionairy = maxTempPerMaaned()
    maxDagligTemperatur = open("max_daily_temperature_2018.csv")
    for linje in maxDagligTemperatur:
        biter = linje.split(",")
        #Bruker .split(",") igjen for å skildre mellom innhold. I den nye filen er temperaturene på plassen 2, og det er derfor biter[2] blir riktig plassering
        if maxTempPerMaanedDictionairy[biter[0]]<float(biter[2]):
            maxTempPerMaanedDictionairy[biter[0]]=float(biter[2])
    return maxTempPerMaanedDictionairy

print("")
print("Oppdatert liste:")
print(varmeRekord())

#Import csv gjør at jeg lettere kan skrive csv filer
import csv
#Prosedyre som tar den oppdaterte listen og skriver det til en fil
def nyFil():
    oppdatertOrdbok = varmeRekord()
    nyOppdatertFil = csv.writer(open("oppdatertliste.csv", "w"))
    #.items() blir brukt for å skrive ut hele linjen
    for maaned in oppdatertOrdbok.items():
        nyOppdatertFil.writerow(maaned)

nyFil()
