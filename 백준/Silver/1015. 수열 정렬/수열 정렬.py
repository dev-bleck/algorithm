import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

indexed_A = [(A[i], i) for i in range(N)]
indexed_A.sort()

P = [0] * N

for new_index in range(N):
    original_index = indexed_A[new_index][1]
    P[original_index] = new_index

print(*P)