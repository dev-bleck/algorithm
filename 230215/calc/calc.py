import sys
sys.stdin = open('sample_input.txt')

T = 10
for tc in range(1, T + 1):
    _, inputs = int(input()), input()
    numb_sum = 0
    for numb in inputs:
        if numb.isdigit():
            numb_sum += int(numb)
    print(f'#{tc} {numb_sum}')