# https://projecteuler.net/problem=48

from math import pow

t = 1000
power_series = (n**n for n in range(1,t+1))

s = 0
for n in power_series:
    s += int(str(n)[-10:])

print(str(s)[-10:])