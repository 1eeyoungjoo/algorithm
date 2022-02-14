"""
1954 달팽이 숫자
테스트 케이스 T
달팽이 크기 N

(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)

먼저 x 값만 전진              0에서 3까지(4)         1에서 2까지(2)
x값 고정 y값 전진             1에서 3까지(3)         2에서 2까지(1)
y값 고정 x값 후퇴             2에서 0까지(3)         1에서 1까지(1)
x값 고정 y값 후퇴             2에서 1까지(2)

"""


import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    current = [0, 0]
    start_point = [0, 0]
    num = 1
    while True:
        for i in range(current[1], current[1]+N):
            current[1] += i
            arr[current[0]][current[1]] = num
            num += 1
        N -= 1
        if N == 0:
            break

        for i in range(current[0]+1, current+N):
            current[0] = i
            arr[current[0]][current[1]] = num
            num += 1
        if N == 0:
            break

        for i in range(current[1]-1, current[1]-N-1, -1):
            current[1] = current[1] - i - 1
            arr[current[0]][current[1]] = num
            num += 1
        if N == 0:
            break

        for i in range(current[0]-1, current[0]-N, -1):
            current[0] = current[0]-i-1
            arr[current[0]][current[1]] = num
            num += 1
        N -= 1
        if N == 0:
            break

    print(f'#{tc}')
    for one in arr:
        print(*one)









