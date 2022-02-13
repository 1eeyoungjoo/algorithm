"""
2628 종이자르기
[3, 2]      [4]
=> (순서 정렬)
[2, 3]      [4]
=> (X, Y 종이 크기 추가)
[2, 3, 8]   [4, 10]
=> (앞 요소와의 차로 값 변경)
[2, 1, 5]   [4, 6]

각 배열의 요소를 곱한 가짓수가 자른 종이의 넓이
"""

import sys
sys.stdin = open("input.txt")

X, Y = map(int, input().split())
# area = []
# for i in range(y):
#     area.append([0] * x)

T = int(input())
xs = [] # [3, 2]
ys = [] # [4]
for i in range(T):
    which, where = map(int, input().split())
    if which == 0:
        ys.append(where)
    else:
        xs.append(where)

for i in range(len(xs)-1, 0, -1):
    for j in range(0, i):
        if xs[j] > xs[j+1]:
            xs[j], xs[j + 1] = xs[j+1], xs[j]

for i in range(len(ys)-1, 0, -1):
    for j in range(0, i):
        if ys[j] > ys[j+1]:
            ys[j], ys[j + 1] = ys[j+1], ys[j]

xs.append(X)
ys.append(Y)

for i in range(len(xs)-1, 0, -1):
    xs[i] = xs[i]-xs[i-1]

for i in range(len(ys)-1, 0, -1):
    ys[i] = ys[i]-ys[i-1]

result = 0
for x in xs:
    for y in ys:
        if x*y > result:
            result = x*y
print(result)