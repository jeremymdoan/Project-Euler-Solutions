import numpy as np
import sympy as sp

def spiralArray(s):
    A = np.zeros((s,s))
    center = int(s/2)
    m = center
    n = m
    edge = s-1
    for i in range(s*s):
        A[m][n] = i+1
        if 0<m<edge and 0<n<edge:
            if A[m][n+1] == 0 and A[m+1][n] == 0 and A[m][n-1] == 0 and A[m-1][n] == 0:
                n+=1
            elif A[m][n+1] == 0 and A[m+1][n] == 0 and A[m][n-1] > 0 and A[m-1][n] == 0:
                m-=1
            elif A[m][n+1] == 0 and A[m+1][n] > 0 and A[m][n-1] > 0 and A[m-1][n] == 0:
                m-=1
            elif A[m][n+1] == 0 and A[m+1][n] > 0 and A[m][n-1] == 0 and A[m-1][n] == 0:
                n-=1
            elif A[m][n+1] > 0 and A[m+1][n] > 0 and A[m][n-1] == 0 and A[m-1][n] == 0:
                n-=1
            elif A[m][n+1] > 0 and A[m+1][n] == 0 and A[m][n-1] == 0 and A[m-1][n] == 0:
                m+=1
            elif A[m][n+1] > 0 and A[m+1][n] == 0 and A[m][n-1] == 0 and A[m-1][n] > 0:
                m+=1
            elif A[m][n+1] == 0 and A[m+1][n] == 0 and A[m][n-1] == 0 and A[m-1][n] > 0:
                n+=1
            elif A[m][n+1] == 0 and A[m+1][n] == 0 and A[m][n-1] > 0 and A[m-1][n] > 0:
                n+=1
        else: 
            if n == edge and m > 0:
                m-=1
            elif m == 0 and n > 0:
                n-=1
            elif n == 0 and m < edge:
                m+=1
            elif m == edge and n < edge:
                n+=1
    return A

def diagonals(A):
    B = []
    l = len(A)
    for m in range(l):
        n = l - m - 1
        B.append(A[m][m])
        B.append(A[n][m])
    return list(set(B))

def diagonals2(n):
    D = [1]
    d, l = 1, 1
    for i in range(1,n*2-1):
        d += 2*l
        D.append(d)
        if i%4 == 0:
            l+=1
    return D


odds = (n for n in range(26001, 27001) if not n%2==0)
#odds = [21001, 22001, 23001, 24001, 25001, 26001, 27001]
for o in odds:
    print("trying {0}".format(o))
    B = diagonals2(o)
    P = [i for i in B if sp.isprime(int(i))]
    r = len(P)/len(B)
    print("ration is {0}".format(r))
    if r < .10:
        print("the winning length is {0}".format(o))
        break