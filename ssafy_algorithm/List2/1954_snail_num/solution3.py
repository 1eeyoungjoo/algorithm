"""
1954 달팽이 숫자
아래에서 패턴 찾음

(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)

(y,x) = 기준점. 시작점

    기준점    기준점(new) 횟수         추가로 필요한 조작
x 증가
#1 (0,0) => (0,3)       4  x 증가
                                    N -= 1
                                    기준점 y += 1
y 증가
#2 (1,3) => (3,3)       3  y 증가
                                    기준점 x -= 1
x 감소
#3 (3,2) => (3,0)       3  x 감소
                                    N -= 1
                                    기준점 y -= 1
y 감소
#4 (2,0) => (1,0)       2  y 감소
                                    기준점 x += 1

         --- 여기까지 네 개 한 세트, 이후 반복 ---

#5 (1,1) => (1,2)       2
                                    N -= 1
                                    기준점 y += 1
#6 (2,2)                1
                                    기준점 x -= 1
#7 (2,1)                1

=> 첫 번째 N을 제외하고, 2번 반복 후 N-1
=> N이 0이 될 때까지 4단계 반복, 중단
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # 현재 위치(x, y)를 담아줄 변수 지정
    currentx = 0
    currenty = 0
    # 배열에 입력할 숫자는 1부터 시작
    num = 1
    # 임시 현재 위치 변수
    tmp = 0
    while True:
        # x값 증가할 때
        for x in range(N):
            # 임시 현재 위치 = currentx + x
            tmp = currentx + x
            arr[currenty][tmp] = num
            num += 1
        # for문 횟수 감소를 위해 N-1
        N -= 1
        # 마지막에 currentx = tmp, tmp 값 초기화
        currentx = tmp
        tmp = 0
        # 다음 단계의 시작점을 위해 y값 1 증가
        currenty += 1

        # 바로 앞선 단계에서 N값에 1을 빼줬기 때문에, 0이 되지 않았는지 확인
        if N == 0:
            break
        # y값 증가할 때
        for y in range(N):
            tmp = currenty + y
            arr[tmp][currentx] = num
            num += 1
        # 마지막에 currentx = tmp, tmp 값 초기화
        currenty = tmp
        tmp = 0
        # 다음 단계의 시작점을 위해 x값 1 감소
        currentx -= 1


        # x값 감소할 때
        for x in range(N):
            tmp = currentx-x
            arr[currenty][tmp] = num
            num += 1
        # 마지막에 currentx = tmp, tmp 값 초기화
        currentx = tmp
        tmp = 0
        # 다음 단계의 시작점을 위해 y값 1 감소
        currenty -= 1
        # for문 횟수 감소를 위해 N-1
        N -= 1

        # 바로 앞선 단계에서 N값에 1을 빼줬기 때문에, 0이 되지 않았는지 확인
        if N == 0:
            break
        # y값 감소할 때
        for y in range(N):
            tmp = currenty - y
            arr[tmp][currentx] = num
            num += 1
        # 마지막에 currentx = tmp, tmp 값 초기화
        currenty = tmp
        tmp = 0
        # 다음 단계의 시작점을 위해 x값 1 증가
        currentx += 1


    print(f'#{tc}')
    for one in arr:
        print(*one)