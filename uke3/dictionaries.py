#En samling av fire ulike høyder
# 0->50, 1->76, 2->87, 3->96
hoydeAar = [50,76,87,96]

#But what if 18->179?? da bruker man dict

by = {"Norge":"Oslo", "Tyskland":"Berlin", "Italia":"Roma"}
tlf = {"Norge":47, "Tyskland":49}

#Slår opp som i en liste:
by["Norge"] #Oslo

#Legge til ekstra element
tlf["italia"]=39

#Slå opp i ordboken
print(tlf["Tyskland"]-tlf["Norge"]) #49-47 = 2 (2 skrives ut)

"Norge" in tlf #True
47 in tlf #false (Sjekker kun nøklene!)
