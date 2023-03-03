import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
     arr = [input() for _ in range(5)]
     ans = ''
     for j in range(15):
          for i in range(5):
               # j가 현재 문자열의 길이보다 짧은 경우,
               if j < len(arr[i]):
                         # 즉 범위내에 존재하는 경우
                         ans += arr[i][j]

     print(f'#{test_case} {ans}')