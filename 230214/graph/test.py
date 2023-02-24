import sys
import pprint
sys.stdin = open('sample_input.txt')


def dfs(start):
    stack = [start]

    while stack:
        now = stack.pop()

        if visited[now] == 0:
            visited[now] = 1

            for next_v in range(v, 0, -1):
                if nodes[now][next_v] == 1 and visited[next_v] == 0:
                    stack.append(next_v)

    return visited


t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    nodes_link = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())
    print(nodes_link)
    nodes = [[0] * (v + 1) for _ in range(v + 1)]

    for i in range(e):
        v1, v2 = nodes_link[i][0], nodes_link[i][1]
        nodes[v1][v2] = 1

    visited = [0 for _ in range(v + 1)]

    print(f"#{tc}", end=" ")
    if dfs(s)[g]:
        print(1)
    else:
        print(0)