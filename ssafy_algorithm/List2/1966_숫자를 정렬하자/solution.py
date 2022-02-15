"""
1966 숫자를 정렬하자

T = 테스트 케이스 개수
N = 숫자열의 길이 (5 <= N <= 50)
N개의 숫자열

오름차순으로 정렬하여 출력
"""
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc} {" ".join(map(str, arr))}')