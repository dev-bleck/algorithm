import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dictionary = {}
questions = {}

for i in range(N):
    group = str(input().rstrip())
    number = int(input())
    members = []
    for _ in range(number):
        members.append(str(input().rstrip()))
    dictionary[group] = members

for i in range(M):
    question = str(input().rstrip())
    number = int(input())

    if number == 0:
        answer = sorted(dictionary[f'{question}'])
        for i in answer:
            print(i)
    elif number == 1:
        for k, v in dictionary.items():
            if question in v:
                print(k)