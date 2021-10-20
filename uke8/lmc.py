sum = 0

n = int(input(""))
while n != 0:
    n = n - 1
    sum = sum + int(input(""))

print(sum)
if sum % 2 == 0:
    print("par")
else:
    print("odde")
