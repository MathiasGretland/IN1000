def forekommer(tekst, tegn):
    for i in tekst:
        if i == tegn:
            return True
    return False

print(forekommer("inf1001", "i"))

def uten_repetisjon(tekst):
    ny_tekst = ""
    for i in range(len(tekst)):
        if not forekommer(tekst[0:i], tekst[i]):
            ny_tekst += tekst[i]
    return ny_tekst

print(uten_repetisjon("aababbabbac"))

def antall_forskjellige(tekst):
    return len(uten_repetisjon(tekst))

print(antall_forskjellige("aababbabbac"))
