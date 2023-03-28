import sys
sys.stdin = open('sample_input.txt')

T = int(input())  # test case input

for test_case in range(1, T + 1):
    # N : 컨테이너 수 / M : 트럭 수
    N, M = map(int, input().split())
    # N개의 컨테이너 input, 내림차순 정렬
    containers = sorted(list(map(int, input().split())), reverse=True)
    # M개의 트럭 input, 내림차순 정렬
    trucks = sorted(list(map(int, input().split())), reverse=True)
    # result : 옮겨진 화물의 전체 무게
    result = 0

    for i in range(len(containers)):
        for j in range(len(trucks)):
            # 현재(j번째) 트럭이 현재(i번째) 컨테이너의 값(즉, 화물의 무게)보다 크거나 같으면,
            if trucks[j] >= containers[i]:
                # 컨테이너의 값(화물의 무게)를 결과값에 더한다.
                result += containers[i]
                # 현재(j번째) 트럭은 출발~
                trucks.pop(j)
                # for문의 반복 범위를 초기화 하기 위해 break
                break

    # 옮겨진 화물의 전체 무게 출력
    print(f'#{test_case} {result}')