import sys
input = sys.stdin.readline

S = str(input().rstrip())
lst = []
for i in range(len(S)):
    lst.append(S[i:])

for i in sorted(lst):
    print(i)