# https://projecteuler.net/problem=61

import MathFunctions as mf

def compare_digits(n1, n2):
    digits1 = int(str(n1)[-2:])
    digits2 = int(str(n2)[:2])
    return digits1 == digits2

def is_cyclic(array):
    len_array = len(array)
    A = [array[0]]
    while len(array) > 0:
        num1 = A[-1]
        array.pop(array.index(num1))
        found_one = False
        for num2 in array:
            if compare_digits(num1, num2):
                A.append(num2)
                found_one = True
                break
        if not found_one:
            break
    if len(A) == len_array and compare_digits(A[-1], A[0]):
        return True
    return False

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
                if num_function_dict[num_type](i)> 1000 \
                    and num_function_dict[num_type](i) < 10000 \
             ] \
            for num_type in num_types \
        }

def find_cyclic():
    A = []
    nums_keys = list(nums.keys())
    current_key = nums_keys[0]
    n1 = nums[current_key][0]
    found_it = False
    nums2 = nums.copy()
    while len(nums2) > 0:
        for i in list(nums2.keys()):
            if i == current_key:
                continue
            for n2 in nums2[i]:
                if compare_digits(n1, n2):
                    A.append(n1)
                    found_it = True
                    n1 = n2
                    nums2.pop(i)
                    break
            if found_it:
                break
        if found_it:
            current_key = i
            found_it = False
        else:
            nums2[current_key].pop(0)
            if len(nums2[0]) == 0:
                nums2.pop(0)
            else:
                n1 = nums2[0][0]            
        if (len(nums2) == 0 and len(A) < len(nums)) \
            or (len(A) == len(nums) and not compare_digits(A[0],A[-1])):
            nums2 = nums.copy()
            A = []
            nums_keys = list(nums2.keys())
            current_key = nums_keys[0]
            nums2[current_key].pop(0)
            n1 = nums2[current_key][0]
    return A

                
print(find_cyclic())