tall = [1,2,3,4,5]

teller = 0
while teller < len(tall):
    tall[teller] = tall[teller] * tall[teller]
    teller += 1
print(tall)
