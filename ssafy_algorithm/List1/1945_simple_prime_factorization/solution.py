"""
1945 간단한 소인수분해
테스트 케이스 개수 - T
숫자 N (2<= N <= 10,000,000)
"""


import sys

sys.stdin = open('input.txt')
T = int(input())
numbers = [2, 3, 5, 7, 11]

for tc in range(1, T+1):
    N = int(input())
    counts = []

    for num in numbers:
        tmp = 0
        while N % num == 0:
            N = N / num
            tmp += 1
        counts.append(tmp)

    print(f'#{tc}', end=' ')
    for i in counts:
        print(i, end=' ')
    print('')



