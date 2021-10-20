tall = []

teller = 0
while teller < 5:
    nye_tall = int(input("Tast inn et tall: "))
    tall.append(nye_tall)
    teller += 1

print(tall)

teller = 0
total = 0
while teller < len(tall):
    total += tall[teller]
    teller += 1
print("Sum av tallene i listen: ", total)

teller = 0
print("Tall som er mindre enn 10")
while teller < len(tall):
    if tall[teller] < 10:
        print(tall[teller])
    teller += 1

finnes_fem = False
teller = 0
while teller < len(tall):
    if tall[teller] == 5:
        finnes_fem = True
    teller += 1
if finnes_fem:
    print("Fem finnes i listen")
else:
    print("Fem finnes ikke i listen")
