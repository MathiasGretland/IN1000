from sokk import Sokk
from skuff import Skuff

sokkenLeif = Sokk("Venstre")
sokkenLuff = Sokk("Hoyre")
skuffen = Skuff()

skuffen.settInnSokk(sokkenLeif)
skuffen.sjekkStatus()
skuffen.settInnSokk(sokkenLuff)
skuffen.sjekkStatus()
