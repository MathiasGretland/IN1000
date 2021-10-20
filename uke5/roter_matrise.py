matriseEn = [
[1,4,7],
[2,5,8],
[3,6,9]
]

matriseTo = [
[1,2,3],
[4,5,6],
[7,8,9]
]

def roter(matrise):
    returMatrise = []
    for i in range(0,len(matrise)):
        returMatrise.append([])
        for j in range(0, len(matrise[i])):
            returMatrise[i].append(matrise[j][i])
    return returMatrise

print(roter(matriseTo))
