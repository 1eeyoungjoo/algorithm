"""
6485 삼성시의 버스 노선

5000개 버스 정류장 1~ 5000
T = 테스트 케이스 개수
N = 버스 노선 개수
Ai, Bi = i번째 버스 노선이 가는 정류장 범위
P = 하나의 정수
Cj = P개 만큼 정수  ( 1 ≤ Cj ≤ 5,000 )
"""

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    all_st = [0]*5001 # 전체 버스 정류장
    N = int(input())
    ABs = [list(map(int, input().split())) for n in range(N)]
    P = int(input())
    st_num = [int(input()) for p in range(P)]
    for idx in range(len(ABs)):
        for i in range(ABs[idx][0], ABs[idx][1]+1):
            all_st[i] += 1

    print(f'#{tc}', end=' ')
    for num in st_num:
        print(all_st[num], end=' ')
    print()


