# N : 원소의 갯수
# M : 집합 정보 갯수
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 서로소 집합 표현을 위한 리스트
powerset = [0 for _ in range(N + 1)]
# powerset[i] 원소는 자신이 속한 집합에서 대표하는 원소를 나타낸다

# def make_set(x):
#     powerset[x] = x


# 집합 초기화
for i in range(N + 1):
    # 현재는 각각의 집합들이 자신만을 가지고 있음
    # make_set(i)
    powerset[i] = i


# x 원소가 속한 집합의 대표 원소를 반환하는 함수
def find_set(x):
    while x != powerset[x]:
        x = powerset[x]
    return x


# x, y : 합집합 할 두 집합에 속한 원소
def union(x, y):
    # y번째 원소가 있는 곳에 x값을 넣어 대표하게 함
    powerset[find_set(y)] = find_set(x)


for i in range(M):
    # 두 개의 원소가 속한 각각의 집합을 합집합 한다
    union(arr[i * 2], arr[i * 2 + 1])


# 각 원소들이 속한 집합의 대표원소
print(powerset)

# 각 집합 대표 원소
print(set(powerset))

# 집합의 갯수
print(len(set(powerset)))