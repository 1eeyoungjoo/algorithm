"""
1954 달팽이 숫자
아래에서 패턴 찾음

(y,x) = 기준점.

    기준점    기준점(new)          추가로 필요한 조작
#1 (0,0) => (0,3) 4  x 증가
                                N -= 1
                                기준점 y += 1
#2 (1,3) => (3,3) 3  y 증가
                                기준점 x -= 1
#3 (3,2) => (3,0) 3  x 감소
                                N -= 1
                                기준점 y -= 1
#4 (2,0) => (1,0) 2  y 감소
                                기준점 x += 1

                                --- 여기까지 네 개 한 세트, 이후 반복 ---
#5 (1,1) => (1,2) 2
#6 (2,2)          1
#7 (2,1)          1

"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    currentx = 0
    currenty = 0
    num = 1
    tmp = 0
    while True:
        if N == 0:
            break
        for x in range(N):
            tmp = currentx + x
            arr[currenty][tmp] = num
            num += 1
        N -= 1
        currentx = tmp
        tmp = 0
        currenty += 1


        if N == 0:
            break
        for y in range(N):
            tmp = currenty + y
            arr[tmp][currentx] = num
            num += 1
        currenty = tmp
        tmp = 0
        currentx -= 1


        if N == 0:
            break
        for x in range(N):
            tmp = currentx-x
            arr[currenty][tmp] = num
            num += 1
        currentx = tmp
        tmp = 0
        currenty -= 1
        N -= 1

        if N == 0:
            break
        for y in range(N):
            tmp = currenty - y
            arr[tmp][currentx] = num
            num += 1
        currenty = tmp
        tmp = 0
        currentx += 1


    print(f'#{tc}')
    for one in arr:
        print(*one)