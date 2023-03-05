import sys
sys.stdin = open('sample_input.txt')

for _ in range(4):
    sj1,si1,ej1,ei1,sj2,si2,ej2,ei2 = map(int, input().split())
    if si1 > ei2 or ei1 < si2 or sj1 > ej2 or ej1 < sj2:
        ans = 'd'
    elif ej1 == sj2 or sj1 == ej2:
        if ei1 == si2 or si1 == ei2:
            ans = 'c'
        else:
            ans = 'b'
    elif ei1 == si2 or si1 == ei2:
        ans = 'b'
    else:
        ans = 'a'
    print(ans)