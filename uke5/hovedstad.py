fildata = open("hovedsteder.csv")
hovedsteder = {}
for linje in fildata:
    biter = linje.split()
    land = biter[0]
    by = biter[1]
    hovedsteder[land] = by

landet = input("Skriv et land: ")
print("Hovedstaden er: " + hovedsteder[landet])
