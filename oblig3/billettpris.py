#Lager prosedyren som jeg kaller for tog, tenkte at det passet oppgaven
def tog():
    #Ber brukeren skrive inn alderen
    inp = input("Hva er din alder? ")
    alder = int(inp)

    billettpris = 0

    #If setning som avgjør hvor mye billettprisen er basert på alderen til brukeren
    if alder <= 17:
        billettpris = 30
        print("Du kan kjøpe barnebillet på ", billettpris, "kr")
    elif alder > 17 and alder < 63:
        billettpris = 50
        print("Du kan kjøpe voksenbillet på ", billettpris, "kr")
    elif alder >= 63:
        billettpris = 35
        print("Du kan kjøpe pensjonistbillet på ", billettpris, "kr")

#Kjører prosedyren
tog()


"""
Et problem med denne prosedyren kan være det faktumet at det ikke er noen grense
på hvor gammel en person er. Altså man kan skrive at alderen sin er 200 år,
noe som ikke gir mening da ingen er så gamle.
"""
