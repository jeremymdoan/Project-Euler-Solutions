# https://projecteuler.net/problem=61

import MathFunctions as mf

def first_two_digits(n):
    return int(str(n)[:2])

def last_two_digits(n):
    return int(str(n)[-2:])

def is_cyclic(array):
    result = True
    for i in range(0,len(array)-1):
        if last_two_digits(array[i]) != first_two_digits(array[i+1]):
            result = False
    if last_two_digits(array[-1]) != first_two_digits(array[0]):
        result = False
    return result

def starting_n_num(n=2, dict_num=0):
    is_correct = check_function_dict[n_dict[dict_num]](n)
    while not is_correct:
        n += 1
        is_correct = check_function_dict[n_dict[dict_num]](n)
    return n

def next_n_num(p, dict_num=0):
    num_type = n_dict[dict_num]
    solutions = find_n[num_type](p)
    n = solutions[0] if mf.is_pos_integer(solutions[0]) else solutions[1]
    return num_function_dict[num_type](n+1)

def next_cyclic(n):
    return last_two_digits(n) * 100

n_dict = {
    0: 'triag', 
    1: 'square', 
    2: 'penta', 
    3: 'hexa', 
    4: 'hepta', 
    5: 'octa'
    }
num_function_dict = {
    'triag': mf.triangle_num, 
    'square': lambda n: int(n**2), 
    'penta': mf.pentagonal_num,
    'hexa': mf.hexagonal_num,
    'hepta': mf.heptagonal_num,
    'octa': mf.octagonal_num
    }
check_function_dict = {
    'triag': mf.triangle_check, 
    'square': mf.is_square, 
    'penta': mf.pentagonal_check,
    'hexa': mf.hexagonal_check,
    'hepta': mf.heptagonal_check,
    'octa': mf.octagonal_check
    }
find_n = {
    'triag': lambda p: mf.quadratic_solution(1, 1, -2*p), 
    'square': lambda p: mf.quadratic_solution(1, 0, -p),
    'penta': lambda p: mf.quadratic_solution(3, -1, -2*p),
    'hexa': lambda p: mf.quadratic_solution(2, -1, -p),
    'hepta': lambda p: mf.quadratic_solution(5, -3, -2*p),
    'octa': lambda p: mf.quadratic_solution(3, -2, -p)
}

def cyclic_array(n):
    good = False
    triag_num = 7875 #starting_n_num(1000, 0)
    A = [triag_num for i in range(0,n)]
    while not good:
        A[0] = triag_num
        twos_good = False
        num2 = starting_n_num(next_cyclic(A[0]), 1)
        while not twos_good:
            A[1] = num2
            if last_two_digits(A[0]) != first_two_digits(A[1]):
                break
            threes_good = False
            num3 = starting_n_num(next_cyclic(A[1]), 2)
            while not threes_good:
                A[2] = num3
                if last_two_digits(A[1]) != first_two_digits(A[2]):
                    break
                threes_good = is_cyclic(A)
                if not threes_good:
                    num3 = next_n_num(num3, 2)
                print(A)
            num2 = next_n_num(num2, 1)
            twos_good = threes_good
        triag_num = next_n_num(triag_num, 0)
        good = twos_good
    return A

print(cyclic_array(3))
#print(find_n['square'](2809))
#print(num_function_dict['square'](91))
