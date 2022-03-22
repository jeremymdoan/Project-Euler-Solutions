# https://projecteuler.net/problem=39

import math

def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2

def get_sides(p):
    rt_triangle_sides = []
    c = int(p/2)
    while c >= p/3:
        a = c - 1
        b = p - c - a
        while b <= a:
            if is_right_triangle(a, b, c):
                rt_triangle_sides.append((a, b, c))
            a -= 1
            b += 1
        c -= 1
    return rt_triangle_sides

max = (0,0)
solutions = []
for p in range(1001):
    sides = get_sides(p)
    num_solutions = len(sides)
    if num_solutions > max[1]:
        max = (p, num_solutions)
        solutions = sides

print(max)
print(solutions)