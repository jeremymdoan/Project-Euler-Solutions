# https://projecteuler.net/problem=51

from sympy import  primerange, isprime

def dupes(n):
    return [d for d in str(n) if str(n).count(d) > 1]

def indicies(L, n):
    return [i for i in range(len(L)) if L[i]==n]

def additive(L, length):
    L2 = [0 for i in range(length)]
    for k in L:
        L2[int(k)] = 1
    return int(''.join([str(i) for i in L2])) 

def add_additive(n, d, add_n):
    return [n+add_n*(i) for i in range(0,10-d) if isprime(n+add_n*(i))]

s = 121300
t = 121400

primes_with_dupes = ((str(p), sorted(set(dupes(p)))) for p in primerange(s, t) if len(dupes(p))>1)

pwd_sequences = (add_additive(int(p_w_d[0]), int(p_w_d[1][0]), additive(indicies(p_w_d[0], p_w_d[1][0]), len(p_w_d[0]))) for p_w_d in primes_with_dupes if int(p_w_d[1][0]) < 3)

print([p_s for p_s in pwd_sequences if len(p_s) > 7])
