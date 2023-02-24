import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    print(pizza, 0)
    i = 1
    while pizza.count(0) != M - 1:
        now_pizza = pizza.pop(0)
        now_pizza = now_pizza // 2
        pizza.append(now_pizza)
        if pizza[-1] == 0:
            pizza.pop()
            pizza.append(0)

        print(pizza, i)
        if pizza.count(0) != M - 1:
            break
        i += 1
    # print(pizza.index(1), i)
    # print(now_pizza)

    print(f'#{test_case} {pizza} {i}')