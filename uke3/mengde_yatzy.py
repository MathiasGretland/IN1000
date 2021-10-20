terninger = []
terninger.append(  int(input("Skriv en terningkast, 1-6")) )
terninger.append(  int(input("Skriv en terningkast, 1-6")) )
terninger.append(  int(input("Skriv en terningkast, 1-6")) )
terninger.append(  int(input("Skriv en terningkast, 1-6")) )
terninger.append(  int(input("Skriv en terningkast, 1-6")) )

#Sjekker om man har hus
terning_mengde = set(terninger)
print(len(terning_mengde)==2 and terninger.count(terninger[0]) in [2,3])
