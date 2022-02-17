"""
5431 민석이의 과제 체크하기

T = 테스트 케이스 수
N, K = 수강생 수, 과제 제출한 사람 수
과제 제출한 사람 번호 K개
"""

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    submitted = list(map(int, input().split()))
    counting = [0 for _ in range(N+1)]

    # 과제 제출한 사람의 인덱스에 값 1 추가해주고
   for person in submitted:
        counting[person] = 1

    print(f'#{tc}', end=' ')
    for i in range(1, len(counting)):
        # counting의 값이 0인 인덱스만 출력
        if counting[i] != 1:
            print(f'{i}', end=' ')
    print()


