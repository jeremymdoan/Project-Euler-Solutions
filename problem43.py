# https://projecteuler.net/problem=43

import itertools

PRIME_MAP = {2:2, 3:3, 4:5, 5:7, 6:11, 7:13, 8:17}

special_nums = []

def special_property_check(num):
    for p in range(0,7):
        num_subtring = int(num[p+1:p+4])
        if not num_subtring % PRIME_MAP[p+2] == 0:
            return False
    return True


for seq in itertools.permutations(range(0,10), 10):
    possible_num = ''.join([str(i) for i in seq])
    if possible_num[0] == '0':
        continue
    #print('testing {0}'.format(possible_num))
    if special_property_check(possible_num):
        print('found one: {0}'.format(possible_num))
        special_nums.append(int(possible_num))


print('sum is: {0}'.format(sum(special_nums)))
