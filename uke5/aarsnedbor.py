filen = open("aarsnedbor.csv")

for linja in filen:
    bitene = linja.split()
    maks_regn = 0
    for dagsverdi in bitene:
        regn = float(dagsverdi)
        if regn > maks_regn:
            maks_regn = regn
    print(maks_regn)
