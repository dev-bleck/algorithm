import sys
input = sys.stdin.readline

is_prime = [True] * 1001
# 0, 1 소수 아니기 때문에 False
is_prime[0] = is_prime[1] = False

for i in range(2, int(1000 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1001, i):
            is_prime[j] = False

# 1000 이하 소수 저장
primes = [x for x in range(2, 1001) if is_prime[x]]

for _ in range(int(input())):
    K = int(input())
    found = False

    for i in primes:
        if found:
            break
        for j in primes:
            if found:
                break
            for k in primes:
                if i + j + k == K:
                    print(i, j, k)
                    found = True
                    break

    if not found:
        print(0)