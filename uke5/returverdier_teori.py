def sum(a, b):
    return a + b

x = sum(2, 3)
print(x)

#Printer ut 5


def hent_brukernavn():
    navn = input("Skriv inn brukernavn: ")
    return navn

x = hent_brukernavn()
print(x)

#Ber brukeren skrive inn et navn også returnern navnet som ble skrevet


def jeg_returnerer_ingenting():
    x = 1 + 2

x = jeg_returnerer_ingenting()

print(x)

#Verdien None blir returnert. Dette er fordi Python alltid vil returnere en verdi fra enhver prosedyre, selv om du ikke spesifiserer en returverdi. Vi skriver så ut "None" i terminalen.
