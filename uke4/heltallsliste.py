tall1 = 0
tall2 = 1
tall3 = 2
tall4 = 3
tall5 = 4

print(tall1)
print(tall2)
print(tall3)
print(tall4)
print(tall5)

tall = []

teller = 0
while teller < 5:
    tall.append(teller)
    teller += 1
print(tall)

teller = 0
while teller < 5:
    print(tall[teller])
    teller += 1
