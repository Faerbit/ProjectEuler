primes = []

def is_prime(number):
    for i in primes:
        if number % i == 0:
            return False
    return True

def get_prime(target):
    i = 1
    while(len(primes)< target):
        i += 1
        if is_prime(i):
            primes.append(i)

    return primes[-1]

print(get_prime(10001))
