from number import number
from functools import reduce

number = str(number)

length = 13
adjacent = ""
product = 0

for i in range(0, len(number)-length):
    cur_product = reduce(lambda x, y: x*y, map(lambda x: int(x), number[i:i+length]))
    if (cur_product > product):
        product = cur_product
        adjacent = number[i:i+length]

string = ""

for i in adjacent:
    string += i + " * "

string = string[:-3] + " = " +str(product)
print(string)
