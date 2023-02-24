# sample_input open
import sys
sys.stdin = open('sample_input.txt')

# max 함수 구현
def max(iterable):
    max_value = 0
    for item in iterable:
        if item > max_value:
            max_value = item

    return max_value

T = int(input()) # test_case

for test_case in range(1, T + 1):
    N = int(input())
    route = [0] * 100

    for _ in range(N):
        bus_type, start, end = map(int, input().split())

        for i in range(start, end + 1):
            if bus_type == 1: # 일반
                route[i] += 1 # 모두 정차

            elif bus_type == 2: # 급행
                if start % 2 == 0: # 짝수
                    if i % 2 == 0: # 짝수 번호 정류장 정차
                        route[i] += 1
                if end % 2 == 1: # 해당 조건이 없으면 종착지에 정차를 안함
                    route[end] += 1

                else: # 홀수
                    if i % 2 == 1: # 홀수 번호 정류장 정차
                        route[i] += 1

            elif bus_type == 3: # 광역
                if start % 2 == 0: # 짝수
                    if i % 4 == 0: # 4의 배수 정류장 정차 => 시작점이 4의 배수가 아닐경우 1 증가??
                        route[i] += 1
                else: # 홀수
                    # 3의 배수이면서 10의 배수가 아닌 정류장 정차
                    if i % 3 == 0 and i % 10 != 0:
                        route[i] += 1

    print(f'#{test_case} {max(route)} {route}') # 같은 정류장에 정차하는 최대 노선

