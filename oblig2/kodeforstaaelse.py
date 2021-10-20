"""
Dette er teknisk sett en lovlig kode fordi man lagrer heltallet i en variabel
av int() som er heltall, men koden vil få feilmelding. Dette skydler at i koden
så prøver man å printe ut et heltall med en tekststreng, dette er ikke mulig
når man bruker +
Bytter man ut + med , istedenfor. Vil koden fungere.
"""

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
