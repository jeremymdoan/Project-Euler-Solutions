# https://projecteuler.net/problem=61

import MathFunctions as mf
import time

def compare_digits(n1, n2):
    digits1 = int(str(n1)[-2:])
    digits2 = int(str(n2)[:2])
    return digits1 == digits2

num_function_dict = {
    'triag': mf.triangle_num, 
    'square': lambda n: int(n**2), 
    'penta': mf.pentagonal_num,
    'hexa': mf.hexagonal_num,
    'hepta': mf.heptagonal_num,
    'octa': mf.octagonal_num
    }

num_types = ['triag','square', 'penta','hexa','hepta','octa']

nums = { \
            num_type: [ \
                num_function_dict[num_type](i) \
                for i in range(150) \
                if 1000 < num_function_dict[num_type](i) < 10000 \
                ] \
            for num_type in num_types \
        }

def find_cyclic():
    target_len = len(nums)
    nums_keys = list(nums.keys())
    k = 'triag'
    for n in nums[k]:
        for k1 in nums_keys:
            if k1 == k:
                continue
            for n1 in nums[k1]:
                if compare_digits(n,n1):
                    for k2 in nums_keys:
                        if k2 == k1 or k2 == k:
                            continue
                        for n2 in nums[k2]:
                            if compare_digits(n1,n2):
                                for k3 in nums_keys:
                                    if k3 == k2 \
                                            or k3 == k1 \
                                            or k3 == k:
                                        continue
                                    for n3 in nums[k3]:
                                        if compare_digits(n2,n3):
                                            for k4 in nums_keys:
                                                if k4 == k3 \
                                                        or k4 == k2 \
                                                        or k4 == k1 or \
                                                        k4 == k:
                                                    continue
                                                for n4 in nums[k4]:
                                                    if compare_digits(n3,n4):
                                                        for k5 in nums_keys:
                                                            if k5 == k4 \
                                                                or k5 == k3 \
                                                                or k5 == k2 \
                                                                or k5 == k1 \
                                                                or k5 == k:
                                                                continue
                                                            for n5 in nums[k5]:
                                                                if compare_digits(n4,n5):
                                                                    if compare_digits(n5,n):
                                                                        return [n,n1,n2,n3,n4,n5]

start = time.time()
the_array = find_cyclic()
end = time.time()
the_sum = sum(the_array) if the_array else 0
print(the_array,the_sum, end-start)