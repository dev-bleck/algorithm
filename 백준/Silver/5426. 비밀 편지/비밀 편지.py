import sys
input = sys.stdin.readline

for _ in range(int(input())):
    letter = list(input().rstrip())
    rooted = int(len(letter) ** 0.5)
    board = [[] * rooted for _ in range(rooted)]

    for i in range(rooted):
        board[i] = letter[i * rooted:i * rooted + rooted]

    for i in range(rooted - 1, -1, -1):
        for j in range(rooted):
            print(board[j][i], end='')
    print()