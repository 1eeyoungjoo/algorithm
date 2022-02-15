"""
[S/W 문제해결 기본] 2일차
1210 Ladder 1

테스트 케이스 10개
N = 테스트 케이스의 번호
arr = 100x100의 2차원 배열 제공


기본 아래로 가지만, 양옆 중 한 곳이라도 1이 있다면 타고 이동.
아래로 이동 [1, 0]
오른쪽으로 이동 [0, 1]
왼쪽으로 이동 [0, -1]
인덱스 조심
"""

import sys
sys.stdin = open("input.txt")

def move(idx, arr):
    y = 0       # 시작하는 위치 인덱스의 y는 언제나 0이기에 따로 받지 않았음
    x = idx
    dx = [0, 1, -1]     # 아래, 우, 좌
    dy = [1, 0, 0]      # 아래, 우, 좌

    while y < 99:
        # 오른쪽에 x 인덱스가 존재하고, 값이 1인 경우
        if 0 <= x+dx[1] <= 99 and arr[y+dy[1]][x+dx[1]] == 1:
            # 반복문을 돌릴 때도 새로운 x 인덱스 값이 범위 안인지 확인해야 함 주의
            while 0 <= x+dx[1] <= 99 and arr[y+dy[1]][x+dx[1]] == 1:
                x = x + dx[1]
                # y = y + dy[1]
            # 반복이 끝난 뒤, 한 칸 아래로 내려가 다시 왼쪽으로 가는 것을 방지
            y += 1

        # 왼쪽에 x 인덱스가 존재하고, 값이 1인 경우
        elif 0 <= x+dx[2] <= 99 and arr[y+dy[2]][x+dx[2]] == 1:
            # 반복문을 돌릴 때도 새로운 x 인덱스 값이 범위 안인지 확인해야 함 주의
            while 0 <= x+dx[2] <= 99 and arr[y+dy[2]][x+dx[2]] == 1:
                x = x + dx[2]
                # y = y + dy[2]
            # 반복이 끝난 뒤, 한 칸 아래로 내려가 다시 오른쪽으로 가는 것을 방지
            y += 1

        # 양쪽 값이 0이거나 인덱스가 존재하지 않는 경우 => 아래로 이동
        else:
            # x = x+dx[0]
            y = y+dy[0]

    # 전체 반복문을 빠져나온 경우 -> y = 99, 맨 하단에 도착
    # 해당 위치의 값을 확인
    if arr[y][x] == 2:
        return 1
    else:   # 1인 경우, 내가 찾는 길이 아니기에 0 반환
        return 0

for i in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for idx in range(100):
        if arr[0][idx] == 1: # 1이면 타고 내려가기 시작
            made_it = move(idx, arr)
            # 함수 반환값이 1인 경우, 찾고자 하는 인덱스이므로, result에 인덱스 값 저장
            if made_it == 1:
                result = idx
                break

    print(f'#{N} {result}')


