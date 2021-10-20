def finnInformasjon(ipDesimal, nettverkBits):
    print(f"IP i CIDR-notasjon {ipDesimal}/{nettverkBits}")

    # Finne ip binært
    ipBin = []
    for oktett in ipDesimal.split("."):
        binOktett = bin(int(oktett))
        binOktett = binOktett[2:]
        while len(binOktett) < 8:
            binOktett = f"0{binOktett}"
        ipBin.append(binOktett)
    print("\nIP-adressen binært:")
    print(".".join(ipBin))

    # Finne nettverksmaske
    nettverksmaske = []
    tallFyltInn = 0
    for i in range(4):
        oktett = ""
        for j in range(8):
            if tallFyltInn < nettverkBits:
                oktett += "1"
            else:
                oktett += "0"
            tallFyltInn += 1
        nettverksmaske.append(oktett)
    print("\nNettverksmasken:")
    print(".".join(nettverksmaske))

    # Finne subnettadressen til maskinen binært
    subnettBin = []
    for i in range(4):
        oktettIp = ipBin[i]
        oktettMaske = nettverksmaske[i]

        oktett = bin(int(oktettIp, 2) & int(oktettMaske, 2))[2:]
        while len(oktett) < 8:
            oktett = f"0{oktett}"
        subnettBin.append(oktett)

    # Finne subnettadressen i CIDR-notasjon
    subnettCidr = []
    for oktett in subnettBin:
        subnettCidr.append(str(int(oktett, 2)))
    print("\nSubnettadressen til maskinen i CIDR-notasjon:")
    print(f"{'.'.join(subnettCidr)}/{nettverkBits}")

    # Finne antall adresser i vertsdelen av subnettet
    print("\nAdresser i vertsdelen av subnettet:")
    print(2**(32 - nettverkBits) - 2)

    # Finne nettverksmaske invertert
    nettverksmaskeInvers = []
    for oktett in nettverksmaske:
        nyOktett = ""
        for bit in oktett:
            if bit == "0":
                nyOktett += "1"
            else:
                nyOktett += "0"
        nettverksmaskeInvers.append(nyOktett)

    # Finne kringkastningsadressen til subnettet binært
    kringkastningBin = []
    for i in range(4):
        oktettIp = ipBin[i]
        oktettMaske = nettverksmaskeInvers[i]

        oktett = bin(int(oktettIp, 2) | int(oktettMaske, 2))[2:]
        while len(oktett) < 8:
            oktett = f"0{oktett}"
        kringkastningBin.append(oktett)

    # Finne kringkastningsadressen til subnettet i CIDR-notasjon:
    kringkastningCidr = []
    for oktett in kringkastningBin:
        kringkastningCidr.append(str(int(oktett, 2)))
    print("\nKringkastningsadressen til subnettet i CIDR-notasjon:")
    print(f"{'.'.join(kringkastningCidr)}/{nettverkBits}")


finnInformasjon("255.255.240.0", 20)  # 192.168.0.165/28
