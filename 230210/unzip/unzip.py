import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    string = ''
    n_sum = 0
    for i in range(N):
        s, n = input().split()
        n = int(n)
        string = string + s * n
        n_sum += n
    print(f'#{test_case}')
    for i in range(0, n_sum, 10):
        print(string[i:i+10])
