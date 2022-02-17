"""
3143 가장 빠른 문자열 타이핑

T = 테스트 케이스의 수
A, B = 두 문자열
(A의 길이는 1이상 10,000이하, B의 길이는 1이상 100이하)

문자열 A를 전체 타이핑하기 위해 눌러야 할 키 최솟값 구하기
문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B 전체를 타이핑 할 수 있다.
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    # 타이핑 횟수를 셀 변수
    count = 0
    idx = 0
    # 각 인덱스를 조회하면서
    while len(A) > 0:
        # A의 부분 문자열이 B와 같은 경우
            if A[idx:idx+len(B)] == B:
                # count +1
                count += 1
                # 해당 부분 슬라이싱으로 삭제
                A = A[len(B):]
            # 다른 경우(일반 타이핑) +1
            else:
                # 한 칸 삭제
                A = A[1:]
                count += 1

    print(f'#{tc} {count}')