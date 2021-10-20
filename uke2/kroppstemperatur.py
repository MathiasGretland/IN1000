inp = input("Hva er kroppstemperaturen din akkurat nå?: ")
temperatur = float(inp)

"""
if temperatur < 36.5:
    print("Du har lav kroppstemperatur")
elif temperatur > 36.5 and temperatur < 37.5:
    print("Du har en god kroppstemperatur")
elif temperatur > 37.5:
    print("Du har en høy kroppstemperatur")
"""

if temperatur < 36.5:
    print("Du har lav kroppstemperatur")
elif temperatur > 37.5:
    print("Du har en høy kroppstemperatur")
else:
    print("Du har en god kroppstemperatur")
