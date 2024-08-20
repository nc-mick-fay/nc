
def prime_nums(num):
    primes = []
    for i in range(2, num + 1):  # to start at 2 and include num
        is_prime = True
        j = 2
        while j <= i/2:
            if i % j == 0:
                is_prime = False

            j += 1
        if is_prime:
            primes.append(i)
    print(primes)
    return primes
