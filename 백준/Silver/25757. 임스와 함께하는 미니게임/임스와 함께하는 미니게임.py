import sys
input = sys.stdin.readline

N, G = map(str, input().split())
lst = list(str(input().rstrip()) for _ in range(int(N)))
lst = list(set(lst))

if G == 'Y':
    print(len(lst))
elif G == 'F':
    print(len(lst) // 2)
else:
    print(len(lst) // 3)