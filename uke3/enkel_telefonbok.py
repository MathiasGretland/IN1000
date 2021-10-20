dictionairy = {"Arne":22334455, "Lisa":95959595, "Jonas":97959795, "Peder":12345678}

navn = input("Skriv inn et navn: ")

if navn in dictionairy:
    print("Telefonnummeret til", navn, "er", dictionairy[navn])
else:
    print("Vi har ikke lagret dette nummeret")
