import sys
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


N, M = map(int, input().split(':'))
answer = gcd(N, M)
print(f'{N // answer}:{M // answer}')