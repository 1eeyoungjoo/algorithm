import sys
sys.stdin = open("input.txt")

T = int(input())

def is_subset_0(arr):
    subset = [-1] * 10
    for i in range(1, 1<<10):
        total = 0
        for j in range(10):
            if i & (1<<j):
                total += arr[j]
        if total == 0:
            return 1
    return 0



for tc in range(1, T+1):
    num_set = list(map(int, input().split()))
    result = is_subset_0(num_set)
    print(f'#{tc} {result}')