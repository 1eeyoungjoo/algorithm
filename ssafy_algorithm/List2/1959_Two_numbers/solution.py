"""
1959 두 개의 숫자열
T = 테스트 케이스
N, M = A, B 배열의 길이
Ai
Bj
더 긴쪽의 양끝을 벗어나지 않는 선에서 이동 가능.
서로 마주보는 숫자들 곱한 뒤 합.
최댓값 구하기
"""
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_sum = 0

    if N > M:
        times = N-M+1
        for time in range(times):
            result = 0
            tmp = A[time:time+M]
            for i in range(M):
                result += tmp[i]*B[i]
            if result > max_sum:
                max_sum = result

    elif N == M:
        for i in range(N):
            max += A[i]*B[i]

    else:
        times = M-N+1
        for time in range(times):
            result = 0
            tmp = B[time:time + N]
            for i in range(N):
                result += A[i] * tmp[i]
            if result > max_sum:
                max_sum = result

    print(f'#{tc} {max_sum}')