# https://projecteuler.net/problem=40

fractional_part = ''
i = 1
while len(fractional_part) < 1000001:
    fractional_part += str(i)
    i += 1

constant = int(fractional_part[0])
for n in range(1,7):
    factor_of_ten = (10**n)-1
    constant *= int(fractional_part[factor_of_ten])

print(constant)