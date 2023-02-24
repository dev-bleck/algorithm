# sample_input open
import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # test_case

for test_case in range(1, T + 1):
    N = int(input()) # 색칠할 영역의 개수
    arr = list([0] * 10 for _ in range(10)) # 색칠 여부 확인 위한 리스트 생성 # 둘 다 for 문 쓰기!
    count = 0 # 보라색이 된 칸을 셈

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split()) # 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔

        for j in range(c1, c2 + 1):
            for i in range(r1, r2 + 1):
                arr[i][j] += color # 이중 for문을 사용해 입력받은 왼쪽 위 좌표부터 오른쪽 아래 좌표까지 색칠
                if arr[i][j] == 3:
                    count += 1 # 보라색인 경우 count 1 증가

    print(f'#{test_case} {count}') # 결과값 반환