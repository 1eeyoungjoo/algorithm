'''
4828 min max
테스트 케이스의 수 T (1 <= T <= 50)
양수의 개수 N (5 <= N <= 1000)
양수 aj (1 <= aj <= 1000000)

1. 테스크 케이스 수만큼(T) 반복
2. 양수의 개수만큼 반복하며, min, max 구하기
3. max - min을 형식에 맞게 출력
'''


import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    min_num = numbers[0]
    max_num = numbers[0]
    for i in range(1, N):
        if numbers[i] > max_num:
            max_num = numbers[i]
        if numbers[i] < min_num:
            min_num = numbers[i]
    result = max_num - min_num
    print(f'#{tc} {result}')
