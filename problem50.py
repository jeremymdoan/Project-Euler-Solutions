# https://projecteuler.net/problem=50

from sympy import  primerange, isprime

t = 1000000
prime_ranges = (primerange(i,t) for i in range(t))
max_sum = 0
max_count = 0
for prime_range in prime_ranges:
    count = 0
    sum_of_primes = 0
    for p in prime_range:
        sum_of_primes += p
        count += 1
        if sum_of_primes > t:
            break
        if isprime(sum_of_primes):
           if count > max_count:
               max_count, max_sum = count, sum_of_primes
print(max_count, max_sum)

