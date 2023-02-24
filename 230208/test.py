# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
# print(s1 == s2)
# print(s1 is s2)
# print(s1 == s5)
# print(s1 is s5)
# print(s1 == s4)
# print(s1 is s4)

# string_a = 'a_string ' \
#            'a_string'
# string_b = "b_string " \
#            'b string'
# string_c = '''c_string
# c_string'''
# string_d = """d_string
# d_string"""
# print(string_a)
# print(string_b)
# print(string_c)
# print(string_d)
# print('finish')

# strings = 'Reverse this strings'
# for i in range(1, len(strings) + 1):
#     print(strings[-i], end='')
# print()
# print(strings[::-1])

"""
5
3
1461
4671224
85761
-1
"""

T = int(input())

for test_case in range(1, T + 1):
    word = int(input())
    result = ''

    num_str = '0123456789'  # 문자열로 변환하기 위한 문자열

    while word > 0:  # word의 숫자들을 빼다가 더 뺄게 없을 때까지
        digit = word % 10  # 1의 자리
        result = num_str[digit] + result  # 뒤에 붙이기

        word = word // 10

    is_negative = False  # 음수인지 아닌지 저장해두기
    if word < 0:
        word = word * -1
        is_negative = True

    if is_negative:
        result = '-' + result

    print(f'#{test_case} {result}')
