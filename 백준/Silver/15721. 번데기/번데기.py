import sys
input = sys.stdin.readline

A = int(input())
T = int(input())
S = int(input())
lst = []

i = 2
while len(lst) < 10001:
    lst.append("뻔")
    lst.append("데기")
    lst.append("뻔")
    lst.append("데기")
    for _ in range(i):
        lst.append("뻔")
    for _ in range(i):
        lst.append("데기")
    i += 1

cnt = 0
index = 0
if S == 0:
    for i in range(len(lst)):
        if lst[i] == '뻔':
            cnt += 1
            index = i

        if cnt == T:
            print(index % A)
            break
else:
    for i in range(len(lst)):
        if lst[i] == '데기':
            cnt += 1
            index = i
    
        if cnt == T:
            print(index % A)
            break