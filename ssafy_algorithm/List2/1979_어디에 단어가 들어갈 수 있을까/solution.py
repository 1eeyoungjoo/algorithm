"""
1979 어디에 단어가 들어갈 수 있을까

T = 테스트 케이스 개수
N, K = 가로&세로 길이, 단어의 길이
(5 ≤ N ≤ 15) (2 ≤ K ≤ N)

흰색 1
검은색 0

가로, 세로별로 어디까지 내려가는지 확인 (ladder1과 비슷)
[주의] 가로의 경우 왼쪽, 세로의 경우 위쪽 칸이 검은색인지 확인해야 한다.
"""


import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                # 가로
                # 좌측에 칸이 존재하지 않거나(x=0) 해당 칸이 0(검정색)일 때만 칸수를 구합니다.
                if x - 1 < 0 or arr[y][x - 1] == 0:
                    block = 1
                    tmp_x = x  # 기존 x는 세로 확인할 때 바뀐 값이면 안 되기에 tmp_x 사용
                    # 다음칸이 인덱스 범위 안에 있고, 1(흰색)인 동안 반복 진행
                    while tmp_x + 1 <= N - 1 and arr[y][tmp_x + 1] == 1:
                        block += 1
                        tmp_x += 1
                    # 해당 칸수가 K개면 count 1 증가
                    if block == K:
                        count += 1
                # 세로
                # 위로 칸이 존재하지 않거나(y=0) 해당 칸이 0(검정색)일 때만 칸수를 구합니다.
                if y - 1 < 0 or arr[y - 1][x] == 0:
                    block = 1
                    tmp_y = y  # 통일감을 위해 넣었습니다
                    # 다음칸이 인덱스 범위 안에 있고, 1(흰색)인 동안 반복 진행
                    while tmp_y + 1 <= N - 1 and arr[tmp_y + 1][x] == 1:
                        block += 1
                        tmp_y += 1
                    # 해당 칸수가 K개면 count 1 증가
                    if block == K:
                        count += 1
            else:
                continue
    print(f'#{tc} {count}')