def addisjon(tall1, tall2):
    tall1 = int(tall1)
    tall2 = int(tall2)
    # Regner ut summen av to tall
    return tall1 + tall2


print(addisjon(2, 9))


def subtraksjon(tall1, tall2):
    tall1 = int(tall1)
    tall2 = int(tall2)
    # Regner ut differansen
    return tall1 - tall2


assert subtraksjon(15, 10) == 5
assert subtraksjon(-15, 10) == -25
assert subtraksjon(-5, -5) == 0


def divisjon(tall1, tall2):
    tall1 = int(tall1)
    tall2 = int(tall2)
    # Regner ut kvotienten
    return tall1/tall2


assert divisjon(10, 5) == 2
assert divisjon(-10, 5) == -2
assert divisjon(-10, -5) == 2


def tommerTilCm(antallTommer):
    antallTommer = int(antallTommer)
    assert antallTommer > 0
    # Regner ut hvor mange tommer det er i cm
    antallTommer = antallTommer * 2.54
    return antallTommer


# skriver ut et eksempel tall
print(tommerTilCm(28))

print()

# Prosedyre som ved bruk av input utfører regnestykker ved hjelp av funksjonene som er laget over


def skrivBeregninger():
    print("Utregninger:")
    tall1 = input("Skriv inn tall 1: ")
    tall2 = input("Skriv inn tall 2: ")
    print()
    print("Resultatet av summering: ", addisjon(tall1, tall2))
    print("Resultatet av subtraksjon: ", subtraksjon(tall1, tall2))
    print("Resultatet av divisjon: ", divisjon(tall1, tall2))
    print()
    print("Konvertering fra tommer til cm:")
    tall = input("Skriv inn et tall: ")
    print("Resultat: ", tommerTilCm(tall))


# Kaller på prosedyren for at den skal kjøres
skrivBeregninger()
