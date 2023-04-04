def makeset(x):
    rep[x] = x


# x가 속한 집합의 대표 return
def findset(x):
    # x == rep[x]가 될 때까지
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    # y의 대표 원소가 x의 대표 원소를 가리키도록 함
    rep[findset(y)] = findset(x)


rep = [i for i in range(6)]  # [0, 1, 2, 3, 4, 5]
print(rep)