from math import*

inp = input("Skriv inn en radius\n>")
radius = float(inp)

diameter = 2*radius
areal = pi*radius*radius
omkrets = diameter*pi

print("Diameter: % 10.2f" % diameter)
print("Areal: % 13.2f" % areal)
print("omkrets: % 11.2f" % omkrets)
