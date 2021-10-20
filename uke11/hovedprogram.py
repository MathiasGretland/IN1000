from hamster import Hamster
from hylle import Hylle

hylle = Hylle(3, 3)
hylle.les_inn_fra_fil("info.txt")
hylle.legg_til_naboer()
"""hylle.print_alle_hamstere()"""
print("\n\nDuplikater:", hylle.finn_duplikater())
