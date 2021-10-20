def velkommen(bruker):
    print("Hei", bruker, "til denne funksjonen")

brukernavn = input("Skriv inn ditt brukernavn: ")

velkommen(brukernavn)

def strenginator(streng1, streng2):
    return streng1 + " " + streng2

strengA = "Hei"
strengB = "Verden!"

konkatenert = strenginator(strengA, strengB)
print(konkatenert)
