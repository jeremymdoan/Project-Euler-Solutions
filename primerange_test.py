from sympy import primerange

s = 121300
t = 121400

primes_lengths = []
last_length = 0 
for i in range(10000):
    length = len([p for p in primerange(s,t)])
    if not length == last_length:
        primes_lengths.append(length)
    last_length = length

print(primes_lengths)
