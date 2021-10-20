liste = [6, -4, 7, -2, 8, -3, 9, -11]
minst = liste[0]
for e in liste:
    if e < minst:
        minst = e

print(minst)

stoerst = liste[0]
for i in range(1, len(liste)):
    if liste[i] > stoerst:
        stoerst = liste[i]

print(stoerst)
