"""
[파이썬 S/W 문제해결 기본] 3일차
4861 회문

T = 테스트 케이스 (1≤T≤50)
N, M = 배열의 크기, 회문의 길이 (10≤N≤100, 5≤M≤N)

... 행은 알겠는데, 열이 헷갈리는.
교수님 코드 참고하자.
"""

import sys
sys.stdin = open('input.txt')

def is_pal():
    for i in range(N):
        for j in range(N-M+1):
            string = arr[i][j:j+M]
            for k in range(M//2):
                if string[k] != string[M-k-1]:
                    break
            else:
                print(f'#{tc} {string}')
                return

    new = []
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if arr[j+k][i] != arr[j+M-k-1][i]:
                    break
            else:
                print(f'#{tc}', end=' ')
                for k in range(j, M+j):
                    print(arr[k][i], end='')
                print()
                return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    is_pal()
