import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# 서로 같은 반이였는지 체크하는 리스트
same_class = [[] for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(5):
            if lst[i][k] == lst[j][k]:
                # j가 i와 같은 반이었던 적이 없으면,
                if j not in same_class[i]:
                    # i와 같은 반으로 체크
                    same_class[i].append(j)
                # i가 j와 같은 반이었던 적이 없으면,
                if i not in same_class[j]:
                    # j와 같은 반으로 체크
                    same_class[j].append(i)
                break

# 같은 반인 학생이 가장 많은 학생을 정답으로
cnt = 0
res = 0
for i in range(N):
    if len(same_class[i]) > cnt:
        cnt = len(same_class[i])
        res = i + 1

# 학생 중에 같은 반이었던 적이 하나도 없으면
if res == 0:
    # 가장 앞의 학생인 1번 학생 출력
    print(1)
# 그 외엔 정답 출력
else:
    print(res)