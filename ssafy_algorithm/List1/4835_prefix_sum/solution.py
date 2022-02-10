'''
4835 구간합
테스트 케이스의 수 T (1 <= T <= 50)
정수의 개수 N, 구간의 개수 M (10 <= N <= 100) (2 <= M < N)
정수 ai (1 <= ai <= 10000)

1. 테스크 케이스 수만큼(T) 반복
2. 첫 번째 정수로 (우선) min, max를 설정
    - 구간합을 구하기 위해 for문을 사용 range(0, M)
3. 정수 리스트을 for문으로 순환하면서 구간별 합을 구한다.
    - for문을 돌 때 1부터 N-M 인덱스까지. range(1, N-M+1)
        - 인덱스 범위를 벗어나는 오류를 없애기 위해 위와같이 인덱스 설정
    - 구간합을 구하기 위해 또 하나의 for문을 사용 range(0, M)
        - 반복 시작할 때마다 구간합 변수를 초기화해줄 것.
    - 동시에 min, max값과의 비교도 진행.
3. max-min을 형식에 맞게 출력

'''


import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    prefix_sum = 0
    for i in range(M):
        prefix_sum += numbers[0+i]
    min_sum = prefix_sum
    max_sum = prefix_sum
    for idx in range(1, N-M+1):
        prefix_sum = 0
        for i in range(M):
            prefix_sum += numbers[idx+i]
        if prefix_sum > max_sum:
            max_sum = prefix_sum
        if prefix_sum < min_sum:
            min_sum = prefix_sum
    print(f'#{tc} {max_sum-min_sum}')
