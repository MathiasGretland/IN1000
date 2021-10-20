def antallSifre(heltall):
    return len(str(heltall))


def antallBokstaverIOrd(bokstav, word):
    teller = 0
    for tegn in word:
        if tegn == bokstav:
            teller +=1
        return teller

def lengreEnnTallet(streng, heltall):
    return len(streng) > heltall

heltall = int(input("skriv et tall"))

antallSifre(heltall)
