inp = input("Tast inn et tall:\n> ")
tall = int(inp)

if tall < 10:
    print("Tallet er mindre enn 10")
elif tall > 10 and tall < 20:
    print("Tallet er mellom 10 og 20")
elif tall == 10 or tall == 20:
    print("Tallet er: ", tall)
else:
    print("Tallet er over 20")
