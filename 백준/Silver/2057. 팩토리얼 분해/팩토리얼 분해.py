import sys
from math import factorial
input = sys.stdin.readline

N = int(input())

if N == 0:
    print('NO')
else:
    factorials = sorted([factorial(i) for i in range(21)], reverse=True)
    for i in factorials:
        if N >= i:
            N -= i

    print('YES') if N == 0 else print('NO')