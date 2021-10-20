#Oppgave A
class Student:
    def __init__(self, brukerNavn):
        self._brukerNavn = brukerNavn
        self._emner = []

    def hentBrukernavn(self):
        return self._brukerNavn

#Oppgave B
class Emne:
    def __init__(self, emneKode):
        self._emneKode = emneKode
        self._aktiviteter = []

    def leggTilAktivitet(self, nyAkt):
        self._aktiviteter.append(nyAkt)

#Oppgave C
class Dato:
    def __init__(self, dag, maaned, aar):
        self._dag = dag
        self._maaned = maaned
        self._aar = aar

    def absoluttDato(self):
        dato = 0
        dato += self._maaned*10000
        dato += self._dag*100
        dato += self._aar
        return dato #Står i oppgaven at rekkefølgen blir måned, år og dato, men i eksempelet så blir det måned, dag og år. Derfor tar jeg også måned, dag og år

    def __str__(self):
        tekst = ""
        tekst = str(self._dag) + "."
        if self._maaned == 9:
            tekst += " september "
        elif self._maaned == 10:
            tekst += " oktober "
        elif self._maaned == 11:
            tekst += " november "
        elif self._maaned == 12:
            tekst += " desember "
        tekst += "20" + str(self._aar)
        return tekst

#Oppgave D
class Aktivitet:
    def __init__(self, emne, dato, aktivitetsnummer):
        self._emne = Emne(emne)
        self._dato = Dato(dato)
        self._aktivitetsnummer = aktivitetsnummer
        self._regStudentWeb = []
        self._regOppMote = []

    def leggTilRegistrertStudent(self, student):
        self._regStudentWeb.append(Student(student))

    def registrerOppmote(self, student):
        self._regOppMote.append(Student(student))

    def skrivUtOppmoteStudenter(self):
        nyListe = []
        for i in self._regStudentWeb:
            nyListe.append(i)
        for o in self._regOppMote:
            nyListe.append(o)
        print("Her er alle som har møtt opp:" + nyListe)

    def absoluttDato(self):
        return self._dato.absoluttDato()

    def oppmote(self):
        nyListe = []
        for i in self._regStudentWeb:
            nyListe.append(i)
        for o in self._regOppMote:
            nyListe.append(o)
        return len(nyListe)

    def __str__(self):
        tekst = ""
        tekst += "Emne: " + str(self._emne)
        tekst += "Nummer: " + str(self._aktivitetsnummer)
        tekst += "Antall oppmøte: " + str(self.oppmote())
        return tekst

#Oppgave E
class Undervisningsadministrasjon:
    def __init__(self):
        self._emner = {}
        self._datoer = {}
        self._studenter = {}

#Oppgave F
    def lesFraFil(self, filnavn):
        fil = open(filnavn)

        for linje in fil:
            biter = linje.split()
            emnekode = biter[0]
            gruppe = Emne(biter[1])
            aar = biter[2]
            maaned = biter[3]
            dag = biter[4]
            datoObjekt = Dato(dag, maaned, aar)
            absolutt = datoObjekt.absoluttDato()
            self._emner[emnekode] = gruppe
            self._dato[absolutt] = datoObjekt

#Oppgave G
    def lesFraFilStudent(self, filnavn):
        fil = open(filnavn)

        for linje in fil:
            biter = linje.split()
            brukernavn = Student(biter[0])
            emnekode = biter[1]
            gruppe = biter[2]
            aktiviteter = self._emner[emnekode] = gruppe
            self._studenter[brukernavn] = aktiviteter

#Oppgave H
    def skrivGrupperMedHoytOppmoete(self, antall):
        grupper = []
        if self.oppmote() > antall:
            grupper.append(self)
        return grupper
