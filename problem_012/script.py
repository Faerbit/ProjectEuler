def get_triangle_number(index):
    return sum(range(1, index+1))

def get_factors(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    return factors

length = 120
i = 1
while True:
    factors = get_factors(get_triangle_number(i))
    if len(factors) >= length:
        print(str(get_triangle_number(i)) + ": " + str(factors))
        break
    i += 1
