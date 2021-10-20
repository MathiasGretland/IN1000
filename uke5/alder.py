min_fil = open("alder.csv")
eldste_alder = 0
eldste_navn = ""
for linje in min_fil:
    biter = linje.split(":")
    navn = biter[0]
    alder = int(biter[1])
    if alder > eldste_alder:
        eldste_navn = navn
        eldste_alder = alder

print(eldste_navn)
