import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    my_sum = 0
    my_len = 0
    for num in nums:
        my_sum += num
        my_len += 1
    result = round(my_sum / my_len)
    print(f'#{tc} {result}')

# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1
