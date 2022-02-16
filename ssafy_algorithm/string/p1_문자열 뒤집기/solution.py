import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    s = input()

    # 슬라이싱 역순 (한방)
    print(f'#{tc} {s[::-1]}')


    # 슬라이싱 역순 (하나하나)
    print(f'#{tc}', end=' ')
    for i in range(len(s), 0, -1):
        print(s[i-1:i], end='')
    print()


    # 인덱스 역순 조회, 추가
    new = ''
    for i in range(len(s)-1, -1, -1):
         new += s[i]
    print(f'#{tc} {new}')


    # 리스트 인덱스 역순
    lst = list(s)
    print(f'#{tc}', end=' ')
    for i in range(len(s)-1, -1, -1):
        print(lst[i], end='')
    print()


    # 리스트 역순 + join
    for i in range(len(lst)//2):
        lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
    print(f'#{tc} {"".join(map(str, lst))}')


    # 리스트 reverse + join
    lst = list(s)
    lst.reverse()
    print(f'#{tc} {"".join(map(str, lst))}')