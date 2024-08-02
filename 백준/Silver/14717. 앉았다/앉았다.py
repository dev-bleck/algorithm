import sys
input = sys.stdin.readline
from itertools import combinations

A, B = map(int, input().split())
score = 0
if A == B:
    score = A * 10
else:
    score = (A + B) % 10
    
arr = [i for i in range(1, 11) for _ in range(2)]
arr.remove(A)
arr.remove(B)
arr_comb = list(combinations(arr, 2))

for i in range(len(arr_comb)):
    if arr_comb[i][0] == arr_comb[i][1]:
        arr_comb[i] = arr_comb[i][0] * 10
    else:
        arr_comb[i] = (arr_comb[i][0] + arr_comb[i][1]) % 10

cnt = 0
for i in range(len(arr_comb)):
    if sorted(arr_comb)[i] >= score:
        break
    cnt += 1
    
print('%.3f' % (cnt / len(arr_comb)))