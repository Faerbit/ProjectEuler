from math import pow

limit = 1000

for c in range(limit-3, 3, -1):
    for b in range(limit-c-1, 2, -1):
        a = limit-c-b
        if (pow(a, 2) + pow(b, 2) == pow(c, 2)):
            print("a: " + str(a) + " b: " + str(b) + " c: " + str(c) + " Produkt: " + str(a*b*c))
