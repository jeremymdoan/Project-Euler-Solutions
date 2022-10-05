import math

def is_pos_integer(n):
    return  n >= 1 and n/int(n) == 1.0

def is_square(n):
    return is_pos_integer(math.sqrt(n))

def quadratic_solution(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    return (sol1, sol2)
    
def triangle_check(p):
    solutions = quadratic_solution(1, 1, -2*p)
    sol1, sol2 = solutions[0], solutions[1]
    return is_pos_integer(sol1) or is_pos_integer(sol2)
    
def pentagonal_check(p):
    solutions = quadratic_solution(3, -1, -2*p)
    sol1, sol2 = solutions[0], solutions[1]
    return is_pos_integer(sol1) or is_pos_integer(sol2)

def hexagonal_check(p):
    solutions = quadratic_solution(2, -1, -p)
    sol1, sol2 = solutions[0], solutions[1]
    return is_pos_integer(sol1) or is_pos_integer(sol2)

def heptagonal_check(p):
    solutions = quadratic_solution(5, -3, -2*p)
    sol1, sol2 = solutions[0], solutions[1]
    return is_pos_integer(sol1) or is_pos_integer(sol2)

def octagonal_check(p):
    solutions = quadratic_solution(3, -2, -p)
    sol1, sol2 = solutions[0], solutions[1]
    return is_pos_integer(sol1) or is_pos_integer(sol2)

def triangle_num(n):
    return int((n/2)*(n+1))

def pentagonal_num(n):
    return int((n/2)*(3*n-1))

def hexagonal_num(n):
    return int(n*(2*n-1))

def heptagonal_num(n):
    return int((n/2)*(5*n-3))

def octagonal_num(n):
    return int(n*(3*n-2))

