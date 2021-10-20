def finnAlleFibTall(tallMax):
    fibListe = []
    tall1 = 0
    tall2 = 1

    fibListe.append(tall1)

    while tall2 <= tallMax:
        fibListe.append(tall2)
        tmpTall = tall1 + tall2
        tall1 = tall2
        tall2 = tmpTall

    return fibListe

def laBrukerSkriveInnTall():
    tallStr = input("Skriv inn et tall: ")
    tall = int(tallStr)
    return tall

x = laBrukerSkriveInnTall()

liste = finnAlleFibTall(x)

for tall in liste:
    print(tall)
