import sys
sys.stdin = open('sample_input.txt')


def answer(p, page):  # count 횟수를 반환하는 함수
    left = 1  # 왼쪽 페이지
    right = p  # 오른쪽 페이지
    count = 0  # while문이 1번 돌 때마다 count 1 증가
    while left <= right:  # 왼쪽 페이지가 오른쪽 페이지가 작은 동안 반복
        center = (left + right) // 2  # 중간 페이지
        if arr[center] == page:  # 현재 페이지가 찾는 페이지랑 같으면 반복문 중단
            break
        elif arr[center] > page:  # 현재 페이지가 찾는 페이지보다 크면 센터를 오른쪽 페이지로
            right = center
            count += 1  # count 1 증가
        else:  # 현재 페이지가 찾는 페이지보다 작으면
            left = center  # 센터를 왼쪽 페이지로
            count += 1  # count 1 증가
    return count


T = int(input())  # test_case input

for test_case in range(1, T + 1):
    P, pA, pB = map(int, input().split())  # 전체 페이지, A의 찾는 페이지, B의 찾는 페이지 input
    arr = [i for i in range(P)]  # 전체 페이지만큼의 배열 생성

    # count 값을 비교해서 결과 출력
    if answer(P, pA) < answer(P, pB):
        print(f'#{test_case} A')
    elif answer(P, pA) > answer(P, pB):
        print(f'#{test_case} B')
    elif answer(P, pA) == answer(P, pB):
        print(f'#{test_case} 0')