def itoa(num):
    new = ''

    # for i in str(num):
    #     new += i

    # sample 문자열 내 '각 숫자 == 인덱스 숫자'
    sample = '0123456789'
    idx = []

    # 음수면 -을 붙여주고 시작
    if num < 0:
        new += '-'
        num = -num

    # 숫자를 1의 자리부터 거꾸로 idx에 추가
    while num > 0:
        num, x = divmod(num, 10)
        idx.append(x)

    # idx 리스트를 반대로 순회하며 new 문자열에 더해주기
    for i in range(len(idx)-1, -1, -1):
        new += sample[idx[i]]

    return new


import sys
sys.stdin = open("input.txt")

T = 6
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {itoa(N)} {type(itoa(N))}')