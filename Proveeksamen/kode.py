class Emne:
    def __init__(self, emnekode, studenter, rettere):
        self._emnekode = emnekode
        self._studenter = studenter
        self._rettere = rettere
        self._obliger = {}

    def administrer(self):
        print(self._emnekode)

        muligheter = ["O", "F", "L", "A"]

        valg = ""

        while valg not in muligheter:
            print("skriv O for å opprette obliger")
            print("skriv F for å starte retting")
            print("skriv L for å lage eksamensliste")
            print("skriv A for å avslutte programmet")

            valg = input().strip().upper()

            if valg == "O":
                self._opprettOblig()
            elif valg == "F":
                self._startRetting()
            elif valg == "L":
                self._skrivEksamensliste()
            elif valg == "A":
                return

    def _opprettOblig(self):
        obligid = "oblig" + str(len(self._obliger))

        print("Lager", obligid, "nå...")
        dato = input("Når er fristen på obligen? ")

        oblig = Oblig(obligid, dato)
        self._obliger[obligid] = oblig

    def _startRetting(self):
        dato = input("Hva er dagens dato? ")

        for obligid in self._obliger:
            oblig = self._obliger[obligid]

            if oblig.klarForRetting(dato):
                besvarelse = oblig.hentBesvarelser(obligid)

                resultater = oblig.fordelRetting(besvarelser, self._rettere)

                for brukernavn in resultater:
                    resultat = resultater[brukernavn]

                    student = Student(brukernavn, brukernavn)

                    self._studenter[brukernavn] = student

                    student.resultat[obligid] = resultat

    def _skrivEksamensliste(self):
        alleGodkjent = []

        for brukernavn in self._studenter:
            student = self._studenter[brukernavn]

            if student.altGodkjent(len(self._obliger)):
                alleGodkjent.appennd(brukernavn)

        print("Her er alle studentene som har fått godkjent")

        for student in alleGodkjent:
            print(student)

class Student:
    def __init__(self, brukernavn, navn):
        self._brukernavn = brukernavn
        self._navn = navn
        self._resultater = {}

    def registrer(self, oblig, resultat):
        self._resultater[oblig] = resultat

    def altGodkjent(self, antObliger):
        if len(self._resultater) < antObliger:
            return False
        else:
            for oblig in self._resultater:
                resultat = self._resultater[oblig]

                if resultat != 1:
                    return False
            return True

class Retter:
    def __init__(self, brukernavn):
        self._brukernavn = brukernavn

    def vurder(self, filnavn):
        return 1

class Oblig:
    def __init__(self, id, frist):
        self._id = id
        self._frist = frist
        #Antat at den ikke er rettet og setter den derfor boolsk False
        self._retter = False

    def klarForRetting(self, dato):
        if self._frist < dato and self._retter == False:
            return True
        return False

    def hentBesvarelser(self, filnavn):
        ordbok = {}

        fil = open(filnavn)

        for linje in fil:
            biter = linje.split()
            brukernavn = biter[0]

            if len(biter) == 2:
                besvarelse = biter[1]
                orbok[brukernavn] = besvarelse
            if len(biter) == 1:
                ordbok[brukernavn] = ""

        return ordbok

    def fordelRetting(self, besvarelser, rettere):
        resultater = {}
        retternummer = 0
        besvarelse_per_rettere = int(len(besvarelse) / len(rettere))

        for besvarelse in besvarelser:
            besvarelse = besvarelser[brukernavn]

            retter = rettere[retternummer]
            resultat = retter.vurder(besvarelse)

            resultater[brukernavn] = resultat

            retternummer += 1
            if retternummer == len(rettere):
                retternummer = 0

        self._rettet = True
        return resultater








self = Emne("kekw", 23, 23)
self.administrer()
