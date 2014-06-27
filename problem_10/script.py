limit = 2 * pow(10, 6)

primes = []

sieve = [False]*(limit + 1)

for i, val in enumerate(sieve):
    if not (i == 0 or i == 1):
        if (val == False):
            primes.append(i)
            for j in range(i, len(sieve), i):
                sieve[j] = True

print(sum(primes))
