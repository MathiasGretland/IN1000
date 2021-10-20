innlest = input("Hvor gammel er du? ")
alder = int(innlest)

while alder>=0:
    if alder > 6:
        print("Velkommen til mitt program")
    else:
        print("Gå heller ut og lek i skogen")

    innlest = input("Hvor gammel er du? ")
    alder = int(innlest)
