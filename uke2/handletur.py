"""
print("Hei! Velkommen til IFI-butikken.")


brod = 20
melk = 15
ost = 40
youghurt = 12

inpBrod = input("Hvor mange brød vil du ha?\n> ")
brod = int(inpBrod)*brod

inpMelk = input("Hvor mange melk vil du ha?\n> ")
melk = int(inpMelk)*melk

inpOst = input("Hvor mange ost vil du ha?\n> ")
ost = int(inpOst)*ost

inpYoughurt = input("Hvor mange youghurt vil du ha?\n> ")
youghurt = int(inpYoughurt)*youghurt

print("du skal betale: ", brod+melk+ost+youghurt, "kr")
"""

pris_broed = 20
pris_melk = 15
pris_ost = 40
pris_youghurt = 12

sum = 0

print("Hei! Velkommen til IFI-butikken.")
inp = input("Hvor mange brød vil du ha?\n> ")
sum+= int(inp)*pris_broed

inp = input("Hvor mange melk vil du ha?\n> ")
sum+= int(inp)*pris_melk

inp = input("Hvor mange ost vil du ha?\n> ")
sum+= int(inp)*pris_ost

inp = input("Hvor mange youghurt vil du ha?\n> ")
sum+= int(inp)*pris_youghurt

print("Du skal betale:", sum, "kr.")
