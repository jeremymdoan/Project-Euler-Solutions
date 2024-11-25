# https://projecteuler.net/problem=60
# stole the idea for nested loops from here: 
# # https://radiusofcircle.blogspot.com/2016/10/problem-60-project-euler-solution-with.html

import sympy as sp
from itertools import combinations
import time

start = time.time()

limit = 10000

def concate(a,b):
    return int(str(a)+str(b))

def test_prime_concat(a, b):
    is_prime = False
    if sp.isprime(concate(a, b)) and sp.isprime(concate(b, a)):
        #print('found a composite')
        is_prime = True
    return is_prime

def prime_set():
    for a in sp.primerange(3, limit):
        for b in sp.primerange(a+1, limit):
            if test_prime_concat(a,b):
                for c in sp.primerange(b+1, limit):
                    if test_prime_concat(a,c) and test_prime_concat(b,c):
                        for d in sp.primerange(c+1, limit):
                            if test_prime_concat(a,d) and test_prime_concat(b,d) and test_prime_concat(c,d):
                                for e in sp.primerange(d+1, limit):
                                    if test_prime_concat(a,e) and test_prime_concat(b,e) and test_prime_concat(c,e) and test_prime_concat(d,e):
                                        return [a,b,c,d,e]

P = prime_set()
print('set is {0} and sum is {1}'.format(P, sum(P)))

end = time.time()

print("run time is {0}".format(end-start))