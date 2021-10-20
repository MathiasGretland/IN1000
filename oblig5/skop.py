"""
Først defineres funksjonen minFunksjon, som ikke tar inn noen parametere. Så defineres prosdeyren hovedprogram, som heller ikke tar inn noen parametere. deretter kalles hovedprogram. inne i hovedprogram opprettes variabelen a med verdi 42. Så opprettes en variabel b med verdi 0, som så blir printet ut til terminalen. Så blir variabelen b gjort om slik at verdien er lik verdien til variabel a, altså 42. Så blir a gjort om til å kalle på funksjonen minFunksjon. Her blir det en for loop som sier at hver x skal kjøre opp til 2, men x er ikke definert som gjør at verdien dens blir gitt 0, altså ingenting. Så blir det opprettet en ny variabel c med verdi 2, som også blir printet ut til terminalen.
Så blir c pluss erlik 1 som betyr at den får verdien 3. Så blir det opprettet en ny variabel med navn b med verdi 10. Men så vil det skje en feil, fordi her skal b pluss erlik a, men inne i funksjonen minFunksjon så er ikke a definert. Derfor vil den ikke printe ut noe, og return verdien blir satt til 'none'. Og derfor vil den heller ikke kunne printe ut b og a i prosedyren hovedprogram, fordi a og b har da value 'none'
"""


def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)


def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)


hovedprogram()
