"""
I denne oppgaven er det laget en liste over ulike allergier som deltakere kan ha.
Den har da også en ordbok hvor det er lagret navnet til deltakere og hva de er allergisk mot.
til slutt skriver den ut hvilke allergier basert på allergiene til deltakerne som
man må holde seg unna.
"""

#Liste som inneholder ulike allergier
allergiListe = ["gluten", "soya", "nøtter", "egg", "fisk", "hvete", "peanøtter", "skjell"]
#Printer ut lista på en forståelig måte
print("Her kommer det en oversikt over hvilke allergier som kan forekomme: ", allergiListe)
#Tom linje
print()

#Her er en ordbok som definerer deltakeren og hva deltakeren er allergisk mot
deltakere = {"geir":"gluten", "ruth":"nøtter", "albert":"egg", "isabell":"hvete"}

#Variabel som kun viser innholdverdien til orboken
deltakereAllergi = deltakere.values()
#Printer ut hvilke allergier man ikke bør ha i maten
print("Ut i fra hva de påmeldte har oppgitt så viser det seg at vi må holde oss unna mat som inneholder", deltakereAllergi)
