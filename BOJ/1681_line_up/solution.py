"""
1681 줄 세우기

학생 수 N, 기피하는 숫자 L
(1 <= N <= 1000000) (0 <= L <= 9)
"""

import sys
sys.stdin = open('input.txt')

N, L = input().split()
count = 0
num = 0
while count < int(N):
    num += 1
    if L in str(num) :
        continue
    else :
        count += 1
print(num)