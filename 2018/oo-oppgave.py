class Hytte :
	def __init__(self, navn, antS, pris) :
		self._navn = navn
		self._antSenger = antS
		self._pris = pris
		
	def hentNavn(self) :
		return self._navn
		
	def totPris(self, antP) :
		return self._pris*antP
		
	def sjekkPlass (self, antP) :
		return antP <= self._antSenger
		
	def __str__(self) :
		s = self._navn + ": " + str(self._antSenger) + " senger; "
		s += str(self._pris) + " kroner per natt."
		return s
	
	def __eq__(self, annen) :
		return self._navn == annen.hentNavn()
		
class Tur :
	def __init__(self, hytteliste, beskr) :
		self._hytter = hytteliste
		self._beskrivelse = beskr
		
	def skrivTur(self) :
		print("\n" + self._beskrivelse)
		for hytte in self._hytter :
			print(hytte)			# her kalles __str__ metoden i Hytte-klassen
		
	def sjekkPrisPlass(self, antP, maks) :
		totKost = 0
		for hytte in self._hytter :
			if not hytte.sjekkPlass(antP) :
				return False
			totKost += hytte.totPris(antP)
			if totKost > maks :
				return False
		return True
		
	def hentAntHytter (self) :
		return len(self._hytter)

# tilsammen finner dere her verktøy/ eksempler for å lese filer med
# ulike formater, og bygge opp strukturer med lister og ordbøker:
class Turplanlegger :
	def __init__(self, hyttefil, turfil) :
		self._hytter = self._hytterFraFil(hyttefil)
		self._turer = self._turerFraFil(turfil)
		
	def _hytterFraFil(self, filnavn) :
		hfil = open(filnavn, "r")
		hytter = {}									# ordbok for alle hyttene
		for linje in hfil :
			hdata = linje.strip().split()	# verdier til instansvariable i ett Hytte-objekt
			hytte = Hytte(hdata[0], int(hdata[1]), float(hdata[2]))
			hytter[hdata[0]] = hytte		# hyttenavn som nøkkel, referanse til hytta som verdi
		return hytter
		hfil.close()
		
	def _turerFraFil(self, filnavn)	:
		tfil = open(filnavn,"r")
		turer = []
		linje = tfil.readline().strip()			# sjekk/ les beskrivelse av turen
		while linje != "" :
			linje2 = tfil.readline()				# les hyttene på turen
			hyttenavn = linje2.split()
			hytteliste = []
			for ettNavn in hyttenavn :		# lag liste av hytteobjektene
				hytteliste.append(self._hytter[ettNavn])
			turer.append(Tur(hytteliste, linje)) # nytt Tur-objekt i tur-listen
			linje = tfil.readline().strip()		# sjekk/ les beskrivelse av ny tur
		tfil.close()
		return turer
		
	def finnTurer(self, antP, maksB, maksD) :
		for tur in self._turer :
			if (tur.hentAntHytter() <= maksD
				and 	tur.sjekkPrisPlass(antP, maksB)) :
					tur.skrivTur()
			
def hovedprogram() :
	turplaner = Turplanlegger("hytter.txt", "turer.txt")
	turplaner.finnTurer(7, 7000, 5)
	
hovedprogram()

	
		
		