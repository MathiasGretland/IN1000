from random import randint

antall_kast = 0
suksess = 0
while antall_kast < 10000:
    kast1 = randint(1,6)
    kast2 = randint(1,6)
    sum = kast1+kast2
    if sum>=10:
        suksess += 1
    antall_kast += 1

print(suksess / antall_kast)
