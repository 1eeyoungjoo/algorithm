import sys
sys.stdin = open('input.txt')
for tc in range(1, 11) :
    width = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(2, width-2) :
        for j in range(arr[i], 0, -1):
            if j > arr[i-1] and j > arr[i-2] and j > arr[i+1] and j > arr[i+2]:
                count += 1
            else :
                continue
    print(f'#{tc} {count}')