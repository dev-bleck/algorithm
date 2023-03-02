# 16진수 2진수로 바꾸기
# 01D06079861D79F99F

arr = input()
for x in arr:
    num = int(x, 16)  # 16진수를 10진수로 변환
    for j in range(3, -1, -1):
        bit = 1 if num &(1<<j) else 0
        print(bit, end='')
    print(' ', end='')
