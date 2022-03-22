# https://projecteuler.net/problem=47

from sympy import factorint
import itertools

t = 1000000
d = 4
consecutive_nums = [0 for i in range(d)]
qualifying_nums = (n for n in range(2,t) if len(factorint(n))==d)
for num in qualifying_nums:
    for i in range(1,d):
        consecutive_nums[i-1] = consecutive_nums[i]
    consecutive_nums[d-1] = num
    if consecutive_nums[-1] - consecutive_nums[0] == d-1:
        print(consecutive_nums)
        break