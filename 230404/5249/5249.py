import sys
sys.stdin = open('sample_input.txt')


def findset(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[findset(y)] = findset(x)


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    rep = [i for i in range(V + 1)]
    graph = []

    for _ in range(E):
        v1, v2, w = map(int, input().split())
        graph.append([v1, v2, w])

    graph.sort(key = lambda x: x[2])

    N = V + 1
    s = cnt = 0

    for v1, v2, w in graph:
        if findset(v1) != findset(v2):
            cnt += 1
            s += w
            union(v1, v2)
            if cnt == N - 1:
                break

    print(f'#{test_case} {s}')