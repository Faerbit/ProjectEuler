target = 100
array = range(1, target + 1)

summe = 0

for i in array:
    summe += pow(i,2)

print (summe)
print (pow(sum(array),2))
print (pow(sum(array),2) - summe)
