"""
14696 딱지놀이
별(★) = 4, 동그라미(●) = 3, 네모(■) = 2, 세모(▲) = 1

라운드 수 N (1<= N <= 1000)
A의 총 개수 a, 딱지 그림 a개
B의 총 개수 b, 딱지 그림 b개
"""

import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(N):
    bucket_a = list(map(int, input().split()))
    A = bucket_a[1:]
    bucket_b = list(map(int, input().split()))
    B = bucket_b[1:]

    bucket_a = [0] * 5
    bucket_b = [0] * 5

    for slap in A:
        bucket_a[slap] += 1
    for slap in B:
        bucket_b[slap] += 1

    for i in range(4, 0, -1):
        if bucket_a[i] != bucket_b[i]:
            if bucket_a[i] > bucket_b[i]:
                print('A')
                break
            else:
                print('B')
                break
        else:
            continue
    else:
        print('D')