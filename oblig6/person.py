"""
I denne oppgaven skal jeg lage en klasse med navn Person. Konstruktøren skal ha instansvariablene navn og alder. Det opprettes også en tom liste med navn hobbyer. Så lager jeg metodene leggTilHobby, skrivHobbyer og skrivUt, så skal brukeren få velge å legge til hobbyer som brukeren vil.
"""
#Oppretter klassen Person
class Person:
    #Lager konstruktøren med instansvariablene som jeg trenger
    def __init__(self, navn, alder):
        self._navn = navn
        self._alder = alder
        self._hobbyer = []
        self._hobbyerStreng = ""

    #Legger til en hobby
    def leggTilHobby(self):
        hobby = input("Skriv inn en hobby: ")
        self._hobbyer.append(hobby)

    #Skriver hobbyene over til en tekststreng så det blir mer ryddig
    def skrivHobbyer(self):
        for i in self._hobbyer:
            self._hobbyerStreng += i + " "
        return self._hobbyerStreng

    #Skriver ut informasjon
    def skrivUt(self):
        print(self._navn)
        print(self._alder)
        print(self.skrivHobbyer())
