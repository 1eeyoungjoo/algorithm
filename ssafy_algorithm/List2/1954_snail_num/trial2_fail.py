import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in (1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    startx = 0
    endx = N
    starty = 1
    endy = N
    currentx = 0
    currenty = 0
    num = 1
    while True:
        for x in range(startx, endx): # 0~3
            currentx = x
            arr[currenty][currentx] = num
            num += 1
        endx -= 1
        if num > N**2:
            break

        for y in range(starty, endy): # 1~3
            currenty = y
            arr[currenty][currentx] = num
            num += 1
        starty += 1
        endy -= 1
        if num > N**2:
            break

        for x in range(endx-1, startx-1, -1): # 2~0
            currentx = x
            arr[currenty][currentx] = num
            num += 1
        startx += 1
        if num > N**2:
            break

        for y in range(endy, starty-1, -1):
            currenty = y
            arr[currenty][currentx] = num
            num += 1
        if num > N**2:
            break

    print(f'#{tc}')
    for one in arr:
        print(*one)