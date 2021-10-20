    def __str__(self):
        tekst = ""
        for i in self.rutenett:
            for celle in i:
                tekst += "|" + celle
            tekst += "|\n"
        return tekst

        naboListe = []
        for r in range(0,self.rader):
            for k in range(0,self.kolonner):
                celle = self.rutenett[r][k]

                #Over
                if r > 0:
                    celle = self.rutenett[r-1][k]
                    naboListe.append(celle)
                #Under
                if r < len(self.rutenett) - 1:
                    celle = self.rutenett[r+1][k]
                    naboListe.append(celle)
                #Venstre
                if k > 0:
                    celle = self.rutenett[r][k-1]
                    naboListe.append(celle)
                #Høyre
                if k < len(self.rutenett) - 1:
                    celle = self.rutenett[r][k+1]
                    naboListe.append(celle)
                #Høyre hjørne
                if r > 0 and k < len(self.rutenett) - 1:
                    celle = self.rutenett[r-1][k+1]
                    naboListe.append(celle)
                #Venstre hjørne
                if r > 0 and k > 0:
                    celle = self.rutenett[r-1][k-1]
                    naboListe.append(celle)
                #Venstre kant
                if r < len(self.rutenett) - 1 and k > 0:
                    celle = self.rutenett[r+1][k-1]
                    naboListe.append(celle)
                #Høyre kant
                if r < len(self.rutenett) - 1 and k < len(self.rutenett) - 1:
                    celle = self.rutenett[r+1][k+1]
                    naboListe.append(celle)
        return naboListe

        self.naboListe = []

        #WORKS!! POG
        for r in range(-1,2):
            for k in range(-1,2):
                naboRad = rad + r
                naboKolonne = kolonne + k

                gyldigNabo = True

                if (naboRad) == rad and (naboKolonne) == kolonne:
                    gyldigNabo = False

                if (naboRad) < 0 or (naboRad) >= self.rader:
                    gyldigNabo = False

                if (naboKolonne) < 0 or (naboKolonne) >= self.kolonner:
                    gyldigNabo = False

                if gyldigNabo:
                    self.naboListe.append(self.rutenett[naboRad][naboKolonne])
        return self.naboListe



        #Inneholder alle døde celler som skal få status "levende"
        dodeCeller = []
        #Inneholder alle levende celle som skal få status "død"
        levendeCeller = []
        levendeCelle = 0
        dodeCelle = 0
        for r in range(0,self.rader):
            for k in range(0,self.kolonner):
                celle = self.rutenett[r][k]
                if celle.erLevende() is True:
                    for celle in self.finnNabo(r,k):
                        if celle.erLevende() is True:
                            levendeCelle += 1
                            if levendeCelle < 2:
                                levendeCeller.append(celle)
                            if levendeCelle == 2 or levendeCelle == 3:
                                levendeCeller.append(celle)
                            if levendeCelle > 3:
                                levendeCeller.append(celle)
                if celle.erLevende() is False:
                    for celle in self.finnNabo(r,k):
                        if celle.erLevende() is False:
                            dodeCelle += 1
                            if dodeCelle == 3:
                                dodeCeller.append(celle)
        for celle in levendeCeller:
            celle.settDoed()
        for celle in dodeCeller:
            celle.settLevende()
        self.generasjonsnummer += 1



        #Inneholder alle døde celler som skal få status "levende"
        self.dodeCeller = []
        #Inneholder alle levende celle som skal få status "død"
        self.levendeCeller = []

        for r in range(len(self.rutenett)):
            for k in range(len(self.rutenett[r])):
                naboer = self.finnNabo(r,k)

                self.levendeNaboer = []

                for celler in naboer:
                    if celler.erLevende():
                        self.levendeCeller.append(celler)

                celleObjekt = self.rutenett[r][k]
                hovedCelle = celleObjekt.erLevende()

                if hovedCelle == True:
                    if len(self.levendeNaboer) < 2 or len(self.levendeNaboer) > 3:
                        self.levendeCeller.append(celleObjekt)

                    if len(self.levendeNaboer) == 3 or len(self.levendeNaboer) == 2:
                        self.dodeCeller.append(celleObjekt)

                else:
                    if len(self.levendeNaboer) == 3:
                        self.dodeCeller.append(celleObjekt)
        for celle in self.levendeCeller:
            celle.settDoed()
        for celle in self.dodeCeller:
            celle.settLevende()
        self.generasjonsnummer += 1

print()
print("Denne: ", celle.hentStatusTegn())

for i in self.naboListe:
    brod = i.hentStatusTegn()
    print(brod)
