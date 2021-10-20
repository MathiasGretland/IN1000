flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"],
"sverige" : ["blått", "gult"],
"danmark" : ["rødt", "hvitt"],
"finland" : ["hvitt", "blått"],
"japan" : ["rødt", "hvitt"],
"gabon" : ["grønt", "gult", "blått"],
"storbritannia" : ["rødt", "blått", "hvitt"],
"chile" : ["blått", "hvitt", "rødt"]
}

print(flaggOrdbok)

flaggOrdbok["usa"] = ["blått", "rødt", "hvitt"]

def flagg():
    navn = input("Navnet på et land: ")
    navn = navn.lower()

    if navn in flaggOrdbok:
        print(flaggOrdbok[navn])
    else:
        print("Landet er ikke registrert i ordboken")

flagg()
