maaneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

inp = input("Tast inn et månedsnummer: ")
nr = int(inp)

if nr > 0 and nr < 13:
    print(nr, "-", maaneder[nr-1])
else:
    print("Ugylding månedsnummer")
