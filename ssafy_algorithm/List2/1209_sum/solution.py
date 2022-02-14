"""
1209 sum
100x100의 2차원 배열
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램 작성

각 행
(0,0) + (0,1) + ... + (0,99)  => (i,j)

각 열
(1,0) + (2,0) + ... + (99,0)  => (j,i)

각 대각선
(0,0) + (1,1) + ... + (99,99)   => (i,i)
(0,99) + (1,98) + ... + (99,0)  => (i, 100-i-1)
"""

import sys
sys.stdin = open("input.txt")
T = 10
for time in range(T):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 결과로 반환할 최고값 변수
    max_num = 0

    diagonal1 = 0
    diagonal2 = 0
    for i in range(100):
        # 첫 번째 for문 안에서 row, column 초기화
        row = 0
        column = 0

        for j in range(100):
            # i, j 위치를 바꿔서 for문 한 번에 row, column 받기
            row += arr[i][j]
            column += arr[j][i]
        # 합을 구한 뒤, max_num과 비교
        if row > max_num:
            max_num = row
        if column > max_num:
            max_num = column

        # 대각선은 (j)for문 밖에서 구했습니다. - 한 번만 구하면 되기 때문.
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][100-i-1]

    # for문이 끝나고 마지막으로 대각선과 비교
    if diagonal1 > max_num:
        max_num = diagonal1
    if diagonal2 > max_num:
        max_num = diagonal2

    print(f'#{tc} {max_num}')


