import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
N = lst.pop(0)

for i in range(len(lst)):
    lst[i] = int(str(lst[i])[::-1])

while len(lst) < N:
    lst2 = list(map(int, input().split()))
    for i in lst2:
        lst.append(int(str(i)[::-1]))

for i in sorted(lst):
    print(i)