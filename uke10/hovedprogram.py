from hamster import Hamster
from hylle import Hylle

hylle = Hylle(3, 3)
hylle.les_inn_fra_fil("info.txt")
hylle.print_alle_hamstere()
print(hylle.finn_duplikater())
