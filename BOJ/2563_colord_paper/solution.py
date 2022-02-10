"""
2563 색종이

"""

import sys
sys.stdin = open('input.txt')
papers = int(input())
X = Y = 0
xys = []
for i in range(papers):
    x, y = map(int, input().split())
    xys.append([x, y])
    if x+10 > X:
        X = x+10
    if y+10 > Y:
        Y = y+10

area = []
for y in range(Y):
    area.append([0]*X)

for xy in xys:
    for x in range(xy[0], xy[0]+10):
        for y in range(xy[1], xy[1]+10):
            area[y][x] = 1

sum = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        sum += area[i][j]

print(sum)
