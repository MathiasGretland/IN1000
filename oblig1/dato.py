#Skriver først ut en beskjed slik at brukeren forstår hva programmet går utpå.
print("Her skal du skrive inn to datoer ved bruk av heltall")

print("Her skal du skrive inn den første datoen")
#dato1 variabelen får en verdi som brukeren definerer.
dag1 = int(input("Tast inn en dag: "))
maaned1 = int(input("Tast inn en måned: "))

print("Her skal du skrive inn den andre datoen")
#dato2 variabelen får en verdi som brukeren definerer.
#int() gjør at det kun kan brukes heltall
dag2 = int(input("Tast inn en dag: "))
maaned2 = int(input("Tast inn en måned: "))

#Hvis maaned1 er større enn maaned2 skrives det ut "Riktig rekkefølge!"
if maaned1 > maaned2:
    print("Riktig rekkefølge!")
#Hvis maaned1 er mindre enn maaned2 skrives det ut "Feil rekkefølge!"
elif maaned1 < maaned2:
    print("Feil rekkefølge!")
#Hvis maaned1 og maaned2 har samme verdi, kommer det nye if-sjekker
elif maaned1 == maaned2:
    #Hvis dag1 og dag2 har samme verdi skrives det ut "Samme dato"
    if dag1 == dag2:
        print("Samme dato")
    #Hvis dag1 er større enn dag2 skrives det ut "Riktig rekkefølge!"
    elif dag1 > dag2:
        print("Riktig rekkefølge!")
    #Hvis dag1 er mindre enn dag2 skrives det ut "Feil rekkefølge!"
    elif dag1 < dag2:
        print("Feil rekkefølge!")
