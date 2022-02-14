"""
연습문제2 부분집합의 합 구현
"""


import sys
sys.stdin = open("input.txt")

T = int(input())

def is_subset_0(arr):
    subset = [-1] * 10
    for a in range(2):
        subset[0] = a
        for b in range(2):
            subset[1] = b
            for c in range(2):
                subset[2] = c
                for d in range(2):
                    subset[3] = d
                    for e in range(2):
                        subset[4] = e
                        for f in range(2):
                            subset[5] = f
                            for g in range(2):
                                subset[6] = g
                                for h in range(2):
                                    subset[7] = h
                                    for i in range(2):
                                        subset[8] = i
                                        for j in range(2):
                                            subset[9] = j
                                            tmp = 0
                                            if subset != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
                                                for times in range(10):
                                                    if subset[times] == 1:
                                                        tmp += arr[times]
                                                if tmp == 0:
                                                    return 1
    return 0


for tc in range(1, T+1):
    num_set = list(map(int, input().split()))
    result = is_subset_0(num_set)
    print(f'#{tc} {result}')



