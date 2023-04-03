import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    powerset = [0 for _ in range(N + 1)]


    def make_set(x):
        powerset[x] = x


    for i in range(N + 1):
        make_set(i)


    def find_set(x):
        while x != powerset[x]:
            x = powerset[x]
        return x


    def union(x, y):
        powerset[find_set(y)] = find_set(x)


    for i in range(M):
        if arr[i * 2] > arr[i * 2 + 1]:
            union(arr[i * 2 + 1], arr[i * 2])
        else:
            union(arr[i * 2], arr[i * 2 + 1])

    result = []
    print(powerset)
    # find_set을 돌면 왜 5가 1로 바뀌는가?
    # find_set은 대표 원소(루트 노드)를 반환하는 함수.
    # 6의 자리에 있는 대표 원소 5를 find_set으로 연산하면,
    # 5의 자리에 있는 대표 원소 1을 return 하기 때문.
    for e in powerset:
        result.append(find_set(e))
        print(result)
    # print(set(result))
    # powerset.pop(0)
    # print(f'#{test_case} {arr} {powerset} {len(set(powerset))} {len(set(result)) - 1}')
    print(f'#{test_case} {len(set(result)) - 1}')