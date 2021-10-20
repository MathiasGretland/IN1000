oliste = []
for i in range(5):
    oliste.append("o")

print(oliste)

stjerneliste = []
for i in range(5):
    stjerneliste.append("*")

print(stjerneliste)

rutenett = []

rutenett.append(oliste)
rutenett.append(stjerneliste)
rutenett.append(oliste)



for i in rutenett:
    print(i)
