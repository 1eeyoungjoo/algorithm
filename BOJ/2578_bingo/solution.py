"""
2578 빙고
5*5 배열 내부 [0, 0]으로 만들기
먼저 받은 입력값 arr[0]으로 추가,
다음 사회자가 부르는 입력값이 arr[0]과 일치하면 arr[1]=1

"""
import sys
sys.stdin = open("input.txt")

Cheolsu = []
for i in range(5):
    tmp = list(map(int, input().split()))
    for num in tmp:
        Cheolsu.append([num, 0])

host = []
for i in range(5):
    a, b, c, d, e = map(int, input().split())
    host += a, b, c, d, e

done = 0
for count in range(1, 26):
    for num in Cheolsu:
        if host[count-1] == num[0]:
            num[1] = 1
            break

    while count >= 12:
        bingo = 0
        for i in [0, 1, 2, 3, 4]:
            if Cheolsu[i][1] ==1 and Cheolsu[i+5][1] ==1 and Cheolsu[i+10][1] ==1 and Cheolsu[i+15][1] ==1 and Cheolsu[i+20][1] ==1:
                bingo += 1

        for i in [0, 5, 10, 15, 20]:
            if Cheolsu[i][1] == 1 and Cheolsu[i+1][1] == 1 and Cheolsu[i+2][1] == 1 and Cheolsu[i+3][1] == 1 and Cheolsu[i+4][1] == 1:
                bingo += 1

        if Cheolsu[0][1] == 1 and Cheolsu[6][1] == 1 and Cheolsu[12][1] == 1 and Cheolsu[18][1] == 1 and Cheolsu[24][1] == 1:
            bingo += 1

        if Cheolsu[4][1] == 1 and Cheolsu[8][1] == 1 and Cheolsu[12][1] == 1 and Cheolsu[16][1] == 1 and Cheolsu[20][1] == 1:
            bingo += 1

        if bingo == 3:
            print(count)
            done = 1
            break

    if done == 1:
        break












