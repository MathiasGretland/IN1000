beholdning = {}

rep = "ja"
while rep == "ja":
    groennsak = input("Skriv inn en grønnsak: ")
    antall = input("Hvor mange har du av " + groennsak.lower() + "? ")
    if antall.isdigit():
        beholdning[groennsak] = int(antall)
        rep = input("Vil du legge inn flere groennsaker? ").lower()
    else:
        print("Ugyldig input, jeg ba om et tall!")

for e in beholdning:
    print(e, ":", beholdning[e])
