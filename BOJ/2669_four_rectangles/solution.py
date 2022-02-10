"""
2669 직사각형 네개의 합집합의 면적 구하기

"""

import sys

sys.stdin = open('input.txt')
rectangles = []
X = Y = 0

for i in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    rectangles.append([x1, y1, x2, y2])
    if x2 > X:
        X = x2
    if y2 > Y:
        Y = y2

area = []
for i in range(Y):
    area.append([0]*X)

for rectangle in rectangles:
    for x in range(rectangle[0], rectangle[2]):
        for y in range(rectangle[1], rectangle[3]):
            area[y][x] = 1
sum = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        sum += area[i][j]

print(sum)

