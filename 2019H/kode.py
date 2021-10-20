"""bok = {"a":[3,4,5], "b":[6,7]}
bok["a"].append(8)
print(len(bok["a"]))
"""

"""def funk(a,b):
    return a*b

c = funk(2+3,2)*4
print(c)
"""

"""#Oppgave 3a
def pris_inkl_frakt(varepris):
    if varepris > 1000:
        return varepris
    elif varepris >= 500 and varepris <= 1000:
        return varepris + 50
    elif varepris < 500:
        return varepris + 80

assert pris_inkl_frakt(300) == 380
assert pris_inkl_frakt(600) == 650
assert pris_inkl_frakt(1300) == 1300
"""

"""#Oppgave 3b
def fjern_utsolgte(handleliste, utsolgte):
    nyliste = []
    for vare in handleliste:
        if not vare in utsolgte:
            nyliste.append(vare)
        else:print(vare)
    return nyliste

assert fjern_utsolgte( ["melk", "brus", "pasta"], ["kanel","brus"]) == ["melk", "pasta"]"""

"""
#Oppgave 3c
def samlet_vaksinasjon(krav_hvert_land):
    vaksiner = []
    for krav in krav_hvert_land:
        for vaksine in krav:
            if not vaksine in vaksiner:
                vaksiner.append(vaksine)
    return vaksiner

print(samlet_vaksinasjon([["difteri","tyfoid"],["hepati","difteri"]]))"""

"""
#Oppgave 3d
def forkort_setning(setning,fjern):
    ny_setning = ""
    for ord in setning.split():
        if not ord==fjern:
            ny_setning = ny_setning + ord + " "
    return ny_setning

setning = "en krabbe skal en dag ut av skallet "
setning_v2 = forkort_setning(setning, "en")
setning_v3 = forkort_setning(setning_v2, "skal")
print(setning_v2)
print(setning_v3)
"""

def sjekk_om_fyord(setning, fyord, synonym_liste):
    biter = setning.split()
    for bit in biter:
        for synonym in synonym_liste:
            if bit in synonym and fyord in synonym:
                return True
    return fyord in biter

assert sjekk_om_fyord("spis masse godsaker", "snop",
[["saft","lemonade"],["snacks","snop","godsaker"],["mye","masse"]]) == True
assert sjekk_om_fyord("spis masse godsaker", "godsaker",
[["saft","lemonade"],["snacks","snop","godsaker"],["mye","masse"]]) == True
assert sjekk_om_fyord("spis masse godsaker", "godsaker", []) == True
assert sjekk_om_fyord("spis masse godsaker", "lemonade",
[["saft","lemonade"],["snacks","snop","godsaker"],["mye","masse"]]) ==False
assert sjekk_om_fyord("spis masse godsaker", "agurk", [["mye","masse"],["spis","gomle"],["snacks","snop","godsaker"]]) == False
