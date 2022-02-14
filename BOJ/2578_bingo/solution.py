"""
2578 빙고
5*5 배열 내부 [0, 0]으로 만들기
먼저 받은 입력값 arr[0]으로 추가,
다음 사회자가 부르는 입력값이 arr[0]과 일치하면 arr[1]=1

"""
import sys
sys.stdin = open("input.txt")

def bingo(arr):
    counting = diagonal1 = diagonal2 = 0
    for i in range(5):
        row = col = 0
        for j in range(5):
            row += arr[i][j]
            col += arr[j][i]
        if row == 5:
            counting += 1
        if col == 5:
            counting += 1

        diagonal1 += arr[i][i]
        diagonal2 += arr[i][4-i]
        if diagonal1 == 5:
            counting += 1
        if diagonal2 == 5:
            counting += 1
    return counting


Cheolsu = [list(map(int, input().split())) for _ in range(5)]
host = [list(map(int, input().split())) for _ in range(5)]
counting = [[0]*5 for _ in range(5)]
done = 0
result = 0
for nums in host:
    for num in nums:
        result += 1
        for y in range(5):
            for x in range(5):
                if Cheolsu[y][x] == num:
                    counting[y][x] += 1
            if y >= 2:
                bingo_count = bingo(counting)
                if bingo_count >= 3:
                    print(result)
                    done = 1
                    break
            if done == 1:
                break
        if done == 1:
            break


