"""
[S/W 문제해결 기본] 2일차
1211 Ladder2
100x100배열
tc = 테스트 케이스 번호 (총 10개)
arr = 테스트 케이스 배열

모든 출발점을 검사하여 바닥까지
가장 짧은 이동 거리를 갖는 시작점 x
(복수 개인 경우 가장 큰 x좌표)를 반환하는 코드를 작성

"""


def ladder(idx, arr):
    y = 0
    x = idx
    dy = [1, 0, 0] # 하, 좌, 우
    dx = [0, -1, 1]
    count = 0

    while y < 99:
        # 좌
        if 0 <= x+dx[1] <= 99 and arr[y][x+dx[1]] == 1:
            while 0 <= x+dx[1] <= 99 and arr[y][x+dx[1]] == 1:
                x += dx[1] # -1
                count += 1
            y += 1
            count += 1
        # 우
        elif 0 <= x+dx[2] <= 99 and arr[y][x+dx[2]] == 1:
            while 0 <= x+dx[2] <= 99 and arr[y][x+dx[2]] == 1:
                x += dx[2] # 1
                count += 1
            y += 1
            count += 1
        # 하
        else:
            y += dy[0] # 1
            count += 1
    return count

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    min = 100*100
    result = 0
    for i in range(100):
        if arr[0][i] == 1:
            tmp = ladder(i, arr)
            if tmp <= min:
                min = tmp
                result = i

    print(f'#{tc} {result}')

