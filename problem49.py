# https://projecteuler.net/problem=49

from sympy import isprime, primerange
from itertools import permutations

def seq_to_int(seq):
    return int(''.join([str(i) for i in seq]))    

def prime_seq(values):
    return (seq for seq in permutations(values, 4) if isprime(seq_to_int(seq)))

def prime_seq_2(values):
    prime_sequences = (seq_to_int(seq) for seq in prime_seq(values) )
    return [seq for seq in prime_sequences]

primes = primerange(1000,10000)

for p in primes:
    prime_list = list(set(sorted(prime_seq_2(str(p)))))
    if len(prime_list) < 3 or prime_list[0] == 0:
        continue
    for i in range(len(prime_list)-2):
        for j in range(i+1,len(prime_list)-1):
            diff = prime_list[j] - prime_list[i]
            num = prime_list[j] + diff
            if num in prime_list:
                print(prime_list[i], prime_list[j], num)
