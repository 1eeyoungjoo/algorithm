"""
[파이썬 S/W 문제해결 기본] 2일차
4836 색칠하기

T = 테스트 케이스   ( 1 ≤ T ≤ 50 )
N = 칠할 영역의 개수  ( 2 ≤ N ≤ 30 )
r1, c1, r2, c2, color = 왼쪽 위 모서리 인덱스, 오른쪽 모서리 인덱스, 색상정보
( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강)
color = 2 (파랑)
"""

import sys
sys.stdin = open("input.txt")

# 색칠하기 함수 (꼭지점 정보 info와 칠할 배열(red, blue)을 받습니다)
def coloring(info, sheet):
    # color 제거 후 할당
    y1, x1, y2, x2 = info[0:-1]
    # counting sort의 변형. +1씩 추가하지 않고 그냥 1로 유지했습니다. (중복 제거)
    # y2, x2 위치도 포함해야 하기 때문에 +1
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            sheet[y][x] = 1
    return sheet

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    infos = [list(map(int, input().split())) for _ in range(N)]

    # 색깔 두 개를 따로 칠할 거기 때문에 빈 배열을 두 개 만들어줍니다.
    red = [[0]*10 for _ in range(10)]
    blue = [[0]*10 for _ in range(10)]
    for info in infos:
        # 색깔값 확인, 1이면 빨강, 2(나머지)면 파랑
        if info[-1] == 1:
            red = coloring(info, red)
        else:
            blue = coloring(info, blue)


    result = 0
    # 겹치는 부분 비교하여, 그 개수를 result 변수에 추가
    for y in range(10):
        for x in range(10):
            if red[y][x] == blue[y][x] == 1:
                result +=1

    print(f'#{tc} {result}')
