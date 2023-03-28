# # 1. 순열 구하기
# # nPr : 1 ~ n까지의 숫자 중 r만큼 줄 세우는 것.
# # data라는 리스트가 주어졌을 때,
# # 그 아이템들을 r개 선택해서 줄 세우는 함수 permutations(data, r)
# def permutations(data, r):
#     n = len(data)
#     result = []  # 결과 반환용 리스트(각 순열 하나씩 다 담김)
#     element = []  # 현재 순열 저장용 리스트
#     def recursion(count):  # 실제로 재귀하는 함수. count : 여태까지 고른 횟수
#         # 목표 갯수만큼 골랐을 때
#         if count == r:
#             result.append(tuple(element))  # 순서 고정 목적으로 튜플 사용
#         else:
#             # i는 data의 아이템을 찾기 위한 인덱스
#             for i in range(n):
#                 if data[i] not in element:
#                     element.append(data[i])  # 아직 현재 순열에서 고르지 않은 데이터 저장
#                     recursion(count + 1)
#                     element.pop()  # 재귀함수 반환 후 pop해서 원상복구
#     recursion(0)
#     return result
#
# data = range(10)
# for candidate in permutations(data, 3):
#     # print(permutations(data, 3))
#     print(candidate)
#
# # 내장 라이브러리를 이용한 순열
# from itertools import permutations
# for candidate in permutations(data, 3):
#     print(candidate)


# 2. 조합
# nCr : 1 ~ n까지의 숫자 중 r개를 고르는 것
# data라는 리스트가 주어졌을 때
# 그 아이템들을 r개 (순서 상관없이) 선택하는 함수 combinations(data, r)
def combinations(data, r):
    n = len(data)
    result = []
    element = []
    # start : 몇 번째 원소부터 고를 수 있는지에 대한 변수
    def recursion(start, count):
        if count == r:
            result.append(tuple(element))
        else:
            for i in range(start, n):
                element.append(data[i])
                recursion(i + 1, count + 1)
                element.pop()

    recursion(0, 0)
    return result

data = range(10)
for combination in (combinations(data, 3)):
    print(combination)

# 내장 라이브러리를 이용한 조합
from itertools import combinations
for combination in (combinations(data, 3)):
    print(combination)