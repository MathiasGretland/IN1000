inp = input("Tast inn din inntekt:\n> ")
inntekt = float(inp)

if inntekt < 10000:
    skatt = inntekt*0.1
else:
    skatt = 10000*0.1 + (inntekt - 10000)*0.3
print("skatt: ", skatt)
