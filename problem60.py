# https://projecteuler.net/problem=60

import sympy as sp
from itertools import combinations

def concate(a,b):
    return int(str(a)+str(b))

def test_prime_concat(permu):
    is_prime = True
    for comb in combinations(permu, 2):
        a, b = comb[0], comb[1]
        #print('checking {0} and {1}'.format(concate(a, b), concate(b, a)))
        if not sp.isprime(concate(a, b)) or not sp.isprime(concate(b, a)):
            #print('found a composite')
            is_prime = False
            break
    if is_prime:
        print('this seems to be one: {0}'.format(permu))
    return is_prime

A = []
candidates = []
for permu in combinations(sp.primerange(3, 1000), 4):
    if test_prime_concat(permu):
        candidates.append(permu)

print("we have the following candidates: {0}".format(candidates))
candidates2 = []
for permu in candidates:
    print("testing {0}".format(permu))
    P = list(permu)
    m = max(P)
    i = 0
    for p in sp.primerange(m+1, 1000):
        P2 = P
        P2.append(p)
        i+=1
        if i%1000 == 0:
            print('i = {1}, working on {0}'.format(permu, i))
        is_prime = True
        if test_prime_concat(P2):
            candidates2.append(P2)

for c in candidates2:
    print("for {0} sum is {1}".format(c, sum(list(c))))