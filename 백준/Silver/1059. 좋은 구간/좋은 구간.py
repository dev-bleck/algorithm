import sys

L = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
n = int(sys.stdin.readline())

if n in nums:
    print(0)
else:
    min_val = 0
    max_val = 0
    
    for num in nums:
        if num < n:
            min_val = num
        elif num > n:
            max_val = num
            break

    min_val += 1
    max_val -= 1

    result = (n - min_val) * (max_val - n + 1) + (max_val - n)
    
    print(result)