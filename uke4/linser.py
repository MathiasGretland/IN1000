from random import shuffle
boks = ["v", "v", "h", "h"]
suksess = 0
antall_trekk = 0

while antall_trekk < 10000:
    antall_trekk += 1
    shuffle(boks)
    linse1 = boks[0]
    linse2 = boks[1]
    if linse1 != linse2:
        suksess += 1

print(suksess / antall_trekk)
