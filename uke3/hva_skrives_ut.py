vest = ["Hallo", "Bergen"]
midt = ["Trondheim"]
print(vest + midt)
#Hallo Bergen Trondheim

nord = ["Alta", "Kautekeino"]
vest = nord + vest
print(vest)
#Alta Kautekeino Hallo Bergen

nord.append("Narvik")
print(nord)
#Alta Kautekeino Narvik

lengde = len(vest+nord)
print(lengde)
#7
