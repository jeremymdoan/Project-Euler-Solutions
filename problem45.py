# https://projecteuler.net/problem=45

from  MathFunctions import  pentagonal_check, hexgonal_check, get_triangle_num

t = 100000

def pentagonal_hexgonal_check(p):
    return pentagonal_check(p) and hexgonal_check(p)

triangle_nums = (get_triangle_num(n) for n in range(2,t+1))
print([p for p in triangle_nums if pentagonal_hexgonal_check(p)])