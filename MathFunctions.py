import math

def is_pos_integer(n):
    return  n > 0 and n/int(n) == 1.0

def quadratic_solution(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    return (sol1, sol2)
    
def pentagonal_check(p):
    solutions = quadratic_solution(3, -1, -2*p)
    sol1, sol2 = solutions[0], solutions[1]
    return is_pos_integer(sol1) or is_pos_integer(sol2)

def hexgonal_check(p):
    solutions = quadratic_solution(2, -1, -p)
    sol1, sol2 = solutions[0], solutions[1]
    return is_pos_integer(sol1) or is_pos_integer(sol2)

def get_pentagonal_num(n):
    return int((n/2)*(3*n-1))

def get_triangle_num(n):
    return int((n/2)*(n+1))

def is_square(n):
    return is_pos_integer(math.sqrt(n))

