inp = input("Hva er din høyde?: ")
hoyde = int(inp)

if hoyde < 140:
    print("Du er lav.")
elif hoyde > 190:
    print("Du er høy.")
else:
    print("Du er middels.")
