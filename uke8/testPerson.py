from person import Person

def hovedprogram():
    mrSmith = Person("Brad Pitt")
    mrsSmith = Person("Angelina Jolie")

    mrSmith.minStatus()
    # Skal gi output: "Jeg er på sjekker'n"

    mrSmith.bryllup(mrsSmith)
    mrsSmith.bryllup(mrSmith)

    mrSmith.minStatus()
    # Skal gi output: "Beklager, jeg er alt gift med Angelina Jolie"

hovedprogram()
