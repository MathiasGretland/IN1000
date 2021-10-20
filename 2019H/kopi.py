def lagSynonymordbok(listeAvLister):
    ordbok = {}
    for liste in listeAvLister:
        for ord in liste:
            temp = liste.copy()
            temp.remove(ord)
            ordbok[ord] = temp

synonymer = [["a", "e", "i", "o", "u"], ["HOM", "c", "d"], ["y", "HOM"], ["k", "l", "m", "n", "p", "q"], ["x"]]

synomordbok = lagSynonymordbok(synonymer)

assert synomordbok["e"] ==  [ ["a", "i", "o", "u"] ]
