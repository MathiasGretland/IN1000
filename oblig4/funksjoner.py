#lager en funksjon som returnerer to tall addert med hverandre
def adder(tall1,tall2):
    return tall1 + tall2

#Skriver de ut
sum = adder(2, 4)
print("Her er summen av tallene:", sum)
sum = adder(6, 10)
print("Her er summen av tallene:", sum)

#Lager en funksjon som teller hvor mange ganger en bokstav forekommer i en tekst
def tellForekomst(minTekst, minBokstav):
    #Lager en variabel med navn teller som øker med en hver gang bokstaven forekommer
    teller = 0
    for tegn in minTekst:
        if tegn == minBokstav:
            teller +=1
    return teller

#Skriver ut resultatet
minTekst = input("Skriv inn et ord: ")
minBokstav = input("Skriv inn en bokstav (f.eks: a): ")
print("Det finnes", tellForekomst(minTekst,minBokstav), minBokstav, "i ordet", minTekst)
