# https://projecteuler.net/problem=57

from fractions import Fraction
import sys
sys.setrecursionlimit(1500)

def onePlus(n):
    if n == 1:
        return Fraction(1,2)
    else:
        return Fraction(1, 2 + onePlus(n-1))

def squareRoot(n):
    return 1 + onePlus(n)

def isLargerNumerator(f):
    return len(str(f.numerator)) >  len(str(f.denominator))

ratios = (squareRoot(i) for i in range(1,1002))
bigNumerators = []

for r in ratios:
    if isLargerNumerator(r):
        bigNumerators.append(r)

print(len(bigNumerators))
