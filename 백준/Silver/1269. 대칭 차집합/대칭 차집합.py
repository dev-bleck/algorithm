import sys
input = sys.stdin.readline

A, B = map(int, input().split())
A_Numbs = list(map(int, input().split()))
B_Numbs = list(map(int, input().split()))

A_res = list(set(A_Numbs) - set(B_Numbs))
B_res = list(set(B_Numbs) - set(A_Numbs))

print(len(A_res) + len(B_res))