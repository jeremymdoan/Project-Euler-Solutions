# https://projecteuler.net/problem=56

def sumDigits(num):
    return sum([int(i) for i in list(str(num))])

max_sum = 0
for a in range(101):
    for b in range(101):
        this_sum = sumDigits(a**b)
        if this_sum > max_sum:
            max_sum = this_sum
            values = (a,b)

print(values, max_sum)