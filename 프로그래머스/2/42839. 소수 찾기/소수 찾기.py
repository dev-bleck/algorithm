from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    comb_numbs = [set(list(permutations(numbers, i))) for i in range(1, len(numbers) + 1)]
    answer = 0
    res = []
    for i in comb_numbs:
        for j in i:
            if int(''.join(j)) not in res and int(''.join(j)) not in [0, 1]:
                res.append(int(''.join(j)))
    
    for i in res:
        cnt = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 1
        
        if cnt == 0:
            answer += 1
                
    return answer