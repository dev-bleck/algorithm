def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(10))


def fibo_while(n):
    a, b = 0, 1  # fibo(0) == 0, fibo(1) == 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a

print(fibo_while(100000))

memo = [0, 1]


def fibo_memo(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo_memo(n - 1) + fibo_memo(n - 2))
    return memo[n]


print(fibo_memo(998))