import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# swaps : 현재 교환 횟수
# max_swaps : 총 교환 횟수
def play(swaps, max_swaps):
    global current_max
    # current_val : 현재 카드의 순서를 기준으로 금액이 얼마인지
    current_val = int(''.join(card_list))

    if (current_val, swaps) in visited:
        return
    visited.append((current_val, swaps))

    if swaps == max_swaps:
        current_max = max(current_max, current_val)
    else:
        # 여기서 재귀 호출
        # (i, j)를 서로 교환
        for i in range(num_of_cards - 1):
            for j in range(i + 1, num_of_cards):
                # 교환 후
                card_list[i], card_list[j] = card_list[j], card_list[i]
                # 다음 교환으로
                play(swaps + 1, max_swaps)
                # 돌아오면 원상복구
                card_list[i], card_list[j] = card_list[j], card_list[i]


for test_case in range(1, T + 1):
    # ex) 123 1 => [123, 1]
    raw_input = list(input().split())
    card_list = list(raw_input[0])      # 카드를 문자열 리스트로
    max_swaps = int(raw_input[1])       # 최대 교환 횟수

    current_max = 0                     # 최대값 초기화
    num_of_cards = len(card_list)       # 카드 갯수
    visited = []
    play(0, num_of_cards)

    print(f'#{test_case} {current_max}')
