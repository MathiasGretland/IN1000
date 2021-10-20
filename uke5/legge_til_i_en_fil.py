min_fil = open("dikt.txt", "w")
min_fil.write("1 elefant kom masjerende!\n")
for antall in range(2,1000):
    min_fil.write(str(antall) + " elefanter kom masjerende!\n")
min_fil.close()
