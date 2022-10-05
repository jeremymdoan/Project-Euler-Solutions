# https://projecteuler.net/problem=60

import sympy as sp
from itertools import combinations

limit = 2000
limit2 = limit * 30

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


def test_candidate(permu):
    P = list(permu)
    m = max(P)
    i = 0
    is_it = False
    for p in sp.primerange(m+1, limit2):
        P2 = P.copy()
        P2.append(p)
        i+=1
        if i%1000 == 0:
            print('i = {1}, working on {0}'.format(P2, i))
        if test_prime_concat(P2):
            print("for {0} sum is {1}".format(P2, sum(list(P2))))
            is_it = True
            break
    return is_it

for permu in combinations(sp.primerange(3, limit), 4):
    if test_prime_concat(permu):
        if test_candidate(permu):
            print("thats it!")



  