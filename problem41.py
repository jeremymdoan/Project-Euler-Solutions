# https://projecteuler.net/problem=41

from PrimeTests import miller_rabin
import itertools

max = (0, 0) 
for n in range(3,10):
    for seq in itertools.permutations(range(1,n+1), n):
        possible_prime = int(''.join([str(i) for i in seq]))
        if miller_rabin(possible_prime, 40):
            if possible_prime > max[1]:
                max = (n, possible_prime)
print('number of digits: {0}; number: {1}'.format(max[0], max[1]))