def ring(ansattnummer, viderekoblingsliste):
    while viderekoblingsliste[ansattnummer] != -1:
        ansattnummer = viderekoblingsliste[ansattnummer]
    return ansattnummer


print(ring(3,[2,-1,-1,0]))

assert ring(1, [2, -1, -1, 0])==1
assert ring(3, [2, -1, -1, 0]) == 2
