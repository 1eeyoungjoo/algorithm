"""
1970 쉬운 거스름돈
테스트케이스 T
받은 돈 N (10 ≤ N ≤ 1,000,000)
화폐종류 = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
"""


import sys
sys.stdin = open("input.txt")
T = int(input())
bill = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    counting = [0] * len(bill)
    N = int(input())
    for idx in range(len(bill)):
        while N >= bill[idx]:
            N -= bill[idx]
            counting[idx] += 1

    print(f'#{tc}')
    print(*counting)

