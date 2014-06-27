
def divisible(number):
    for i in array:
        if not number % i == 0:
            return False

    return True

array = range(1,20)

done = False
number = 0

while not done:
    number = number + array[len(array)-1]
    if divisible(number):
        break

print (number)
