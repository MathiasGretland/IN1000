min_fil = open("navn.txt")

liste = []

for linje in min_fil:
    liste.append(linje)

min_fil.close()

print(liste)
