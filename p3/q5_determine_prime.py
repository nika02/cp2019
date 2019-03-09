primes = [2]
print(2)
i = 3
print(i)
while len(primes) < 1000:
    for p in primes:
        if (i % p == 0) or (p*p > i):
            break

    if i%p != 0:
        primes.append(i)
        print(i)
    i = i + 2
