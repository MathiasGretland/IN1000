
tall = [1, 5, 2, 6, 3, 7, 2, 6]


minste = tall[0]
stoerste = tall[0]
minste_plass = 0
største_plass = 0

print(tall) 

teller = 1
while teller < len(tall) :
    # Finner minste tall
    if tall[teller] < minste :
        minste = tall[teller]
        minste_plass = teller

    # Finner stoerste tall
    if tall[teller] > stoerste :
        stoerste = tall[teller]
        stoerste_plass = teller

    teller+=1

tmp = tall[minste_plass]
tall[minste_plass] = tall[stoerste_plass]
tall[stoerste_plass] = tmp

print(tall) # Skriver ut etter forandring

print("Stoerste: ", stoerste)
print("Minste: ", minste)
