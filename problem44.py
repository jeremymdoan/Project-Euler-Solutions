# https://projecteuler.net/problem=44

import itertools
from  MathFunctions import  pentagonal_check, get_pentagonal_num

t = 10000
def sum_property(tup):
    j, k = tup[0], tup[1]
    return pentagonal_check(j+k) 

def diff_property(tup):
    j, k = tup[0], tup[1]
    return pentagonal_check(k-j)

pentagonal_nums = (get_pentagonal_num(n) for n in range(1,t+1))

first_pass = (seq for seq in itertools.combinations(pentagonal_nums, 2) if sum_property(seq))

second_pass = (seq for seq in first_pass if diff_property(seq))

print([(seq, seq[1] - seq[0]) for seq in second_pass])