#Ordbok som inneholder beboer, samt. hva de liker å spise til frokost, lunsj og middag
beboerMat = {"ruth":["brød","egg","pølser"], "geir":["grøt","ost","kjøttkaker"], "ingvar":["knekkebrød","toast","suppe"]}

#Lager en prosdeyre som ber om navnet til en beboer, og skriver deretter ut hva den beboeren liker å spise
#Er ikke beboeren i listen, vil den si ifra om at den beboeren ikke er registrert
def beboerMatProsedyre():
    print(beboerMat)

    navn = input("Skriv inn navnet til en beboer: ")
    navn = navn.lower()

    if navn in beboerMat:
        print(beboerMat[navn])
    else:
        print(navn, "er ikke registrert")

#Kaller på prosedyren
beboerMatProsedyre()

"""
3 a) Her ville jeg valgt å bruke mengde, fordi alle har et unikt brukernavn,
og det er derfor ingen grunn til å måtte skrive inn et brukernavn mer enn 1 gang.

3 b) Her ville jeg valgt å bruke orbok, fordi da kan man enkelt kalle på et brukernavn,
og da vil også antall poeng kunne komme opp.

3 c) Her ville jeg valgt å bruke liste, fordi her kan man skrive inn et navn flere ganger.
Selvom det er liten sjanse for å vinne store summer i Lotto flere ganger på et år,
så er det fortsatt mulig.

3 d) Her ville jeg valgt å bruke ordbok, fordi her kan man for eksempel gi nøkkelverdien
navnet på en gjest. også kan da innholdverdien være en ting eller flere som den gjesten
er allergisk mot.
"""
