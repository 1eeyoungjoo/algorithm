"""
1966 숫자를 정렬하자

T= 테스트 케이스 개수
N = 숫자열의 길이 (5 <= N <=50)
N개의 숫자
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(f'#{tc}', end=' ')
    print(*numbers)
