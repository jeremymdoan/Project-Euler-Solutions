# https://projecteuler.net/problem=53

from numpy import math

def combos(n, r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

count = 0
for n in range(23, 101):
    for r in range(n+1):
        c = combos(n,r)
        if c > 1000000:
            count+=1

print(count)