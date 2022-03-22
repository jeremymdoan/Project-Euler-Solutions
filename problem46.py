# https://projecteuler.net/problem=46

from PrimeTests import prime_check

def goldback_calc(n, s):
    return n - 2*s**2

def goldback_check(n):
    remainder = (goldback_calc(n, s) for s in range(1, n-2) if goldback_calc(n, s)>1)
    for i in remainder:
        if prime_check(i):
            #print(n,i, (n-i)/2)
            return True
    return False

t1=1000
t2=10000
odd_composites = (n for n in range(t1,t2) if  not n%2==0 and not prime_check(n))
smallest = 0
for c in odd_composites:
    if not goldback_check(c):
        smallest = c
        break
print(c, smallest)

