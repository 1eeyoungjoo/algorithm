"""
2001 파리 퇴치 - M x N 배열

테스트 케이스 T
N, M (5 <= N <= 15) (2 <= M <= N)
N줄에 걸쳐 N x N 배열
"""

import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    max = 0
    for j in range(N-M+1):
        for k in range(N-M+1):
            tmp = 0
            for inc in range(M):
                for inc2 in range(M):
                    tmp += arr[j+inc][k+inc2]
            if tmp > max:
                max = tmp
    print(f'#{tc} {max}')


