# What is the largest prime factor of the number 600851475143 ?

def find_factors(number):
    divisor = 1
    factors = set()
    while True:
        if number % divisor == 0:
            factors.add(divisor)
            factors.add(number // divisor)
        if divisor*divisor >= number:
            break
        divisor = divisor + 1
    factors = sorted(factors)
    return factors

def find_primes(list):
    primelist = set()
    for x in list:
        for num in range(2, x+1):
            if num == x:
                primelist.add(x)
                continue
            if x % num == 0:
                break
    primelist = sorted(primelist)
    print(primelist[-1])

find_primes(find_factors(600851475143))
