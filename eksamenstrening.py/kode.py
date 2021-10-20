def minst(a, b, c):
    svar = a
    if b <= a and b <= c:
        svar = b
    if c <= a and c <= b:
        svar = c

    return svar


v = minst(120.2, 133.2, 72.1)
print(v)
