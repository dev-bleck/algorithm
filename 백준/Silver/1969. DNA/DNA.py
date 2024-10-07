import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna_list = [str(input().rstrip()) for _ in range(N)]
count = 0
rep_dna = ''

for j in range(M):
    tmp_dna = []
    for i in range(N):
        tmp_dna.append(dna_list[i][j])
    tmp_dna.sort(reverse=False)
    rep_dna += max(tmp_dna, key=tmp_dna.count)

for i in range(N):
    now_count = 0
    for j in range(M):
        if rep_dna[j] != dna_list[i][j]:
            now_count += 1
    
    count += now_count

print(rep_dna)
print(count)