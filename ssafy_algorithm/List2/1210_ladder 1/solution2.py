"""
[S/W 문제해결 기본] 2일차
1210 Ladder 1

교수님의 의사 코드, 팁을 보게 된 뒤의
두 번째 풀이 - 아래에서부터 접근해보자.
"""

import sys
sys.stdin = open("input.txt")

def move(idx, arr):
    y = 99       # 시작하는 위치 인덱스의 y는 언제나 99이기에 따로 받지 않았음
    x = idx
    dx = [0, 1, -1]     # 위, 우, 좌
    dy = [-1, 0, 0]      # 위, 우, 좌

    while y > 0:
        # 오른쪽에 x 인덱스가 존재하고, 값이 1인 경우
        if 0 <= x+dx[1] <= 99 and arr[y+dy[1]][x+dx[1]] == 1:
            # 반복문을 돌릴 때도 새로운 x 인덱스 값이 범위 안인지 확인해야 함 주의
            while 0 <= x+dx[1] <= 99 and arr[y+dy[1]][x+dx[1]] == 1:
                x = x + dx[1]
                # y = y + dy[1]
            # 반복이 끝난 뒤, 한 칸 위로 올라가 다시 왼쪽으로 가는 것을 방지
            y -= 1

        # 왼쪽에 x 인덱스가 존재하고, 값이 1인 경우
        elif 0 <= x+dx[2] <= 99 and arr[y+dy[2]][x+dx[2]] == 1:
            # 반복문을 돌릴 때도 새로운 x 인덱스 값이 범위 안인지 확인해야 함 주의
            while 0 <= x+dx[2] <= 99 and arr[y+dy[2]][x+dx[2]] == 1:
                x = x + dx[2]
                # y = y + dy[2]
            # 반복이 끝난 뒤, 한 칸 위로 올라가 다시 오른쪽으로 가는 것을 방지
            y -= 1

        # 양쪽 값이 0이거나 인덱스가 존재하지 않는 경우 => 위로 이동
        else:
            # x = x+dx[0]
            y = y+dy[0]

    # 전체 반복문을 빠져나온 경우 -> y = 0, 맨 상단에 도착
    # 해당 위치의 x 인덱스를 반환
    return x

for i in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    made_it = -1

    for idx in range(100):
        if arr[99][idx] == 2: # 2이면 타고 올라가기 시작
            made_it = move(idx, arr)

    print(f'#{N} {made_it}')


