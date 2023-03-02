import sys
sys.stdin = open('sample_input.txt')

T = int(input())

code_table = {
    (0, 0, 0, 1, 1, 0, 1): 0,
    (0, 0, 1, 1, 0, 0, 1): 1,
    (0, 0, 1, 0, 0, 1, 1): 2,
    (0, 1, 1, 1, 1, 0, 1): 3,
    (0, 1, 0, 0, 0, 1, 1): 4,
    (0, 1, 1, 0, 0, 0, 1): 5,
    (0, 1, 0, 1, 1, 1, 1): 6,
    (0, 1, 1, 1, 0, 1, 1): 7,
    (0, 1, 1, 0, 1, 1, 1): 8,
    (0, 0, 0, 1, 0, 1, 1): 9,
}


def find_code():
    global ans

    for r in range(N):
        for c in range(M - 1, 55, -1):
            code = arr[r][c:c - 56:-1]

            if code[0] != 1:
                continue

            for nr in range(r, r + 5):
                ncode = code
                if ncode != code:
                    break
            else:
                code = code[:: -1]
                code_valid = 0
                code_sum = 0
                for i in range(8):
                    ni = 7 * i
                    decode = code_table.get(tuple(code[ni:ni + 7]))
                    if decode == None:
                        break
                    else:
                        code_sum += decode
                        if i % 2 == 0:
                            code_valid += decode * 3
                        else:
                            code_valid += decode
                else:
                    if code_valid % 10 == 0:
                        ans = code_sum
                        return


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0

    find_code()

    print(f"#{tc} {ans}")
