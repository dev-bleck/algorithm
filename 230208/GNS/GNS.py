T = int(input())
for test_case in range(1, T + 1):
    numb_and_len = input()
    string = input().split()
    string_len = len(" ".join(sorted(string)))
    numb_dict = {
        0: "ZRO",
        1: "ONE",
        2: "TWO",
        3: "THR",
        4: "FOR",
        5: "FIV",
        6: "SIX",
        7: "SVN",
        8: "EGT",
        9: "NIN"
    }

    for idx in range(len(string)):
        for numb in range(len(numb_dict)):
            if string[idx] == numb_dict.get(numb):
                string[idx] = list(numb_dict.keys())[numb]

    string = sorted(string)

    for idx in range(len(string)):
        for numb in range(len(numb_dict)):
            if string[idx] == list(numb_dict.keys())[numb]:
                string[idx] = numb_dict.get(numb)

    string = " ".join(string)

    print(f"#{test_case}\n{string}")