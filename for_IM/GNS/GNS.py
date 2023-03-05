import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    _ = input()
    arr = input().split()

    numb_dict = {
        "ZRO" : 0,
        "ONE" : 1,
        "TWO" : 2,
        "THR" : 3,
        "FOR" : 4,
        "FIV" : 5,
        "SIX" : 6,
        "SVN" : 7,
        "EGT" : 8,
        "NIN" : 9
    }

    tmp = []
    for i in arr:
        tmp.append(numb_dict[i])
    tmp = sorted(tmp)

    ans = []
    for idx in range(len(tmp)):
        for key, value in numb_dict.items():
            if value == tmp[idx]:
                ans.append(key)

    print(f'#{test_case}', *ans)