import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    for _ in range(100):
        for idx in range(1, M + 1):
            if not pizza or (len(pizza) == 1):
                break
            now_pizza = pizza.pop(0)
            now_pizza = now_pizza // 2
            if now_pizza == 0:
                pass
            else:
                pizza.append(now_pizza)
            print(pizza, idx)

    #
    # print(pizza, i)
    # if pizza.count(1) == 1 and pizza.count(0) == M - 1:
    #     break
    # else:
    #     i += 1

    print(f'#{test_case} {pizza}')