target = 'abcdabcdabcabcef'  # 전체
pattern = 'abcef'  #찾는 것


# Brute Force - for
def brute_force_for(target, pattern):
    target_len = len(target)
    pattern_len = len(pattern)

    # 범위 설정
    for i in range(target_len - pattern_len + 1):  # 패턴 길이가 남는 인덱스까지 검사
        cnt = 0
        for j in range(pattern_len):  # 패턴의 각 문자를 순서대로 검사
            if target[i + j] != pattern[j]:  # 패턴과 일치하지 않으면
                break
            else:
                cnt += 1
        if cnt >= pattern_len:  # 일치한 pattern의 글자수가 pattern의 총 글자수보다 크거나 같다
            return i  # 패턴과 매치되는 타겟의 시작지점 인덱스를 반환
    return -1  # 못 찾음


# Brute Force - while
def brute_force_while(target, pattern):
    target_len = len(target)
    pattern_len = len(pattern)
    # i : target 검사용 인덱스 / j : pattern 검사용 인덱스
    i = j = 0  # while문이기 때문에 직접 인덱스 관리

    # 1. j >= pattern_len이면 성공
    # 2. i >= target_len이면 실패
    while j < pattern_len and i < target_len:
        # 지금 검사 중인 문자가 일치하는가?
        if target[i] != pattern[j]:
            # BF의 방식대로 일치하기 시작한 지점 바로 다음 지점으로
            i = i - j
            # 다음은 0이어야 해서 -1
            j = -1

        # 다음 순회 준비
        i += 1
        j += 1

    if j == pattern_len:
        # 어디까지 갔는지 - 찾는 길이 => 이걸 안하면 찾은 문자 다음으로 인덱스로 가기 때문
        return i - pattern_len
    else:
        return -1


print(brute_force_for(target, pattern))
print(brute_force_while(target, pattern))
