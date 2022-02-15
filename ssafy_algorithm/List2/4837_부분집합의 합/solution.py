"""
[파이썬 S/W 문제해결 기본] 2일차
4837 부분집합의 합
T = 테스트 케이스 ( 1 <= T <= 50 )
N, K = 부분집합 원소의 수, 부분집합의 합 ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )


집합 A, 1부터 12까지의 숫자를 원소로 가진다.
원소 합이 K인 부분집합의 개수 출력
(없을 시 0 출력)
"""
import sys
sys.stdin = open("input.txt")

# 집합 A 설정
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

# 테스트 케이스 개수만큼 반복
for tc in range(1, T+1):
    # N, K = 부분집합 원소의 수, 부분집합의 합
    N, K = map(int, input().split())
    result = 0 # 결과로 출력할 변수 : 조건에 부합하는 부분집합의 개수
    for i in range(0, 1<<12): # 전체 부분집합에 대해 조회
        # 부분집합의 합, 원소 개수를 저장할 변수 설정
        total = 0
        cnt = 0
        for j in range(12):
            # 일치할 경우 -> 해당 요소를 부분집합의 요소로 가지고 있음 의미
            if i & 1<<j:
                # 원소 개수, 합 증가
                cnt += 1
                total += A[j]
        # 각각 N, K와 값이 같다면 -> 우리가 찾고자 하는 부분집합임
        if cnt == N and total == K:
            result += 1

    print(f'#{tc} {result}')

