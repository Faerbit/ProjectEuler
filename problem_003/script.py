import math

number = 600851475143
current = 0

for i in range(3, int(math.sqrt(number)), 2):
    if (number % i == 0):
        print (i)
        number = number / i
        current = i
print ("Biggest prime factor: " + str(current))
