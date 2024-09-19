def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(nums):    
    nums = sorted(nums)
    len_nums = len(nums)
    
    lst = []
    for i in range(len_nums - 2):
        for j in range(i + 1, len_nums - 1):
            for k in range(j + 1, len_nums):
                lst.append(nums[i] + nums[j] + nums[k])
    
    res = 0
    for n in lst:
        if is_prime(n):
            res += 1
    
    return res