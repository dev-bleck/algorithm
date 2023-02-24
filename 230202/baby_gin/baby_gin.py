# sample_input open
import sys
sys.stdin = open('sample_input.txt')

# test case count input
test_case = int(input())
# 1 ~ test case 반복
for tc in range(1, test_case + 1):
    num = int(input())
    c = [0] * 12

    # 카드의 개수만큼 반복
    for i in range(6):
        # num % 10 = 마지막자리의 수 => c 배열에 1 증가
        c[num % 10] += 1
        # 마지막 자리 제거
        num //= 10

    # while 문 인덱스
    i = 0
    # triblet, run 결과
    tri_result = run_result = 0

    while i < 10:
        # triplet 확인
        if c[i] >= 3:
            # 현재 인덱스가 triplet이면 값에서 3을 뺌
            c[i] -= 3
            # triplet 결과 1 증가
            tri_result += 1
            continue  # continue가 없으면 아직 남아있어도 그냥 넘어감
            # ex) 1이 6개 일 때 생각해보면 1번 돌면 1이 3이 되는데 그대로 i += 1이 돼서 i = 2가 됨.
            # 아직 c[1]은 3인데도 불구하고 c[2]를 확인하기 시작.

        # run 확인
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            # 현재 인덱스가 run 이면
            # 현재 인덱스, 현재 인덱스 + 1, 현재 인덱스 + 2의 값에서 1을 뺌
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            # run 결과 1 증가
            run_result += 1
            continue  # 여기의 continue 또한 위와 마찬가지

        # 다음 인덱스를 확인하기 위해 1 증가
        i += 1

    # triplet 결과와 run 결과의 합이 2 이상이면 baby-gin
    if tri_result + run_result == 2:
        # baby-gin이면 결과에 1 할당
        result = 1
    else:
        # baby-gin이 아니면 결과에 0 할당
        result = 0

    # 결과 출력
    print(f'#{tc} {result}')
