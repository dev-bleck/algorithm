A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + A * 1000)
elif A == B != C:
    print(1000 + A * 100)
elif A == C != B:
    print(1000 + A * 100)
elif C == B != A:
    print(1000 + B * 100)
elif A != B and B != C:
    print(max(A, B, C) * 100)