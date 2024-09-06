import sys
input = sys.stdin.readline

N = int(input().rstrip())
numb = 1
result = 0

while numb ** 2 <= N:
    numb += 1
    result += 1
    
print(result)