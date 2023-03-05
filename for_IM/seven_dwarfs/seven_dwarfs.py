import sys
sys.stdin = open('sample_input.txt')



dwarfs = [list(map(int, input().split())) for _ in range(9)]

for a in range(9):
    for b in range(a + 1, 9):
        for c in range(b + 1, 9):
            for d in range(c + 1, 9):
                for e in range(d + 1, 9):
                    for f in range(e + 1, 9):
                        for g in range(f + 1, 9):
                            if sum(dwarfs[a] + dwarfs[b] + dwarfs[c] + dwarfs[d] + dwarfs[e] + dwarfs[f] + dwarfs[g]) == 100:
                                lst = sorted(dwarfs[a] + dwarfs[b] + dwarfs[c] + dwarfs[d] + dwarfs[e] + dwarfs[f] + dwarfs[g])

for i in lst:
    print(i)
