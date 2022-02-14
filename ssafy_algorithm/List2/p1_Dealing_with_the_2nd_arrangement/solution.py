"""
연습문제1 2차원 배열 다루기
기준점 중심으로 상, 하, 좌, 우
dx = [0, +1, 0, -1]
dy = [-1, 0, +1, 0]

=> four_direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]

[주의] 범위를 벗어난 인덱스 값 [주의]
=> 조건문으로 확인할 것
"""

import sys

sys.stdin = open("input.txt")

T = int(input())

# 절대값 구하는 함수 정의
# 계속 사용되는 부분이라 함수로 만들었습니다.
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 현재 위치 기준 사방으로 확인하기 위한 x, y
    four_direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    result = 0 # 출력할 결과값

    # 현재 위치 (x,y)를 뽑기 위한 이중 반복문
    for y in range(5):
        for x in range(5):
            tmp_sum = 0 # 각 줄의 합을 저장할 임시합
            # 사방 x, y에 대해
            for dx, dy in four_direction:
                # x+dx, y+dy가 범위 안일 때만 실행
                if 0 <= x + dx < 5 and 0 <= y + dy < 5:
                    # 두 숫자의 차이를 절대값으로 바꿔서 임시합에 저장
                    tmp_sum += my_abs(arr[y + dy][x + dx] - arr[y][x])
            # for문이 끝났을 때, 출력할 결과값에 더해줍니다.
            result += tmp_sum

    print(f'#{tc} {result}')
