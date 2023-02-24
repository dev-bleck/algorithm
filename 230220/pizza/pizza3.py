import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    now_pizza_index = 1
    while pizza.count(0) != M - 1:
        now_pizza = pizza.pop(0)
        now_pizza = now_pizza // 2
        pizza.append(now_pizza)
        now_pizza_index += 1
        if now_pizza_index == M + 1:
            now_pizza_index = 1
        print(pizza)

    print(f'#{test_case} {now_pizza_index}')

