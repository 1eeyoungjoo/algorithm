"""
13300 13304 방 배정
학생수 N, 한 방에 배정할 수 있는 최대 인원 K (1 <= N, K <= 1000)
성별, 학년이 N개 줄
(여 = 0, 남 = 1)
"""

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = []
for i in range(2):
    arr.append([0]*7)

for i in range(N):
    sex, grade = map(int, input().split())
    arr[sex][grade] += 1

total = 0

for students in arr:
    for student in students:
        if student == 0:
            continue
        quo, rem = divmod(student, K)
        if rem == 0:
            total += quo
        else:
            total += (quo+1)

print(total)