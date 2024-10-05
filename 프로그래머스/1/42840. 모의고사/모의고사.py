def solution(answers):    
    answer = []
    
    answers.insert(0, 0)
    numb_1 = [1, 2, 3, 4, 5]
    numb_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    numb_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count_1 = count_2 = count_3 = 0
    
    for i in range(1, len(answers)):
        if answers[i] == numb_1[i % len(numb_1) - 1]:
            count_1 += 1
        
        if answers[i] == numb_2[i % len(numb_2) - 1]:
            count_2 += 1
        
        if answers[i] == numb_3[i % len(numb_3) - 1]:
            count_3 += 1
    
    max_count = max(count_1, count_2, count_3)
    if count_1 == max_count:
        answer.append(1)
    
    if count_2 == max_count:
        answer.append(2)
    
    if count_3 == max_count:
        answer.append(3)
        
    return answer