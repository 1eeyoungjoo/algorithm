"""
2635 수 이어가기

첫 번째 수 (1<= N <= 30,000)
두 번째 수 -> 양의 정수 중 하나 선택
세 번째 이후 -> 앞의 앞의 수에서 앞의 수를 뺀 수.
음의 정수가 나오면 버리고 종료.
"""

import sys
sys.stdin = open("input.txt")

# 100 99 1 98
# 100 60 40 20 20 0
# 100 62 38 24 14 10 4 6


N = int(input())
arr = [N, N, 0]
count = len(arr)
for second_num in range(1, N+1):
    x = N
    y = second_num
    z = 0
    tmp = [x, y]
    while True:
        z = x-y
        if z < 0:
            break
        else :
            tmp.append(z)
            x = y
            y = z
    if count < len(tmp):
        arr = tmp
        count = len(arr)

print(count)
print(*arr)

# While문 조건을 거는 게 어려워서 결국 While True로 하고 break 조건을 따로 걸었다.
# if문 내부에서 count 숫자도 바꿔줘야 하는데 깜박함.
# arr 초기 설정을 어떻게 해야 할지 모르겠음. arr = []으로 해뒀다가, arr = [N, N, 0]으로 변경....