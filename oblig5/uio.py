print("Hei og velkommen til uio's orbok!")
#Her er orboken hvor alle brukerne og epostene lagres
ordbok = {}

#Funksjon som gjør at brukeren får et automasisk generert brukernavn
def lagBrukernavn(navn):
    fulltNavn = {}
    biter = navn.split(" ")
    fornavn = biter[0]
    etternavn = biter[1]
    fulltNavn[fornavn] = etternavn
    #Setter etternavn[0] slik at kun den første bokstaven blir brukt.
    brukernavn = fornavn+etternavn[0]
    #Lower blir brukt slik at brukernavnene alltid er i små bokstaver
    brukernavn = brukernavn.lower()
    return brukernavn

#Funksjon som lager en epost basert på brukernavn og suffic
def lagEpost(brukernavn, suffix):
    epost = brukernavn+ "@"+ suffix
    return epost

#Prosedyre som printer ut epost basert på brukernavn og epost
def printEposter(brukernavnOgEposter):
    for i in ordbok:
        print(lagEpost(i, ordbok[i]))

#Her er en while løkke som kjører så lenge brukeren ikke oppfører bokstaven "s"
tekst = ""
while tekst != "s":
    tekst = input("Tast i for å legge til en bruker, tast p for en oversikt, og tast s for å avslutte: ")
    #Lager en ny bruker basert på ny informasjon fra brukeren, denne nye informasjonen blir kjørt gjennom lagBrukernavn funksjonen som lager en ny bruker med epost
    if tekst == "i":
        navn = input("Skriv inn et navn (Eks: Tone Damli): ")
        suffix = input("Skriv inn en suffix(Eks: uio.no): ")
        brukernavn = lagBrukernavn(navn)
        ordbok[brukernavn] = suffix
    #Printer ut eposter basert på informasjonen som er i ordboken ordbok
    elif tekst == "p":
        print("")
        printEposter(ordbok)
        print("")
