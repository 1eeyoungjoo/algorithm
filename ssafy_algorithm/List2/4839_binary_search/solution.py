"""
[파이썬 S/W 문제해결 기본] 2일차
4839 - 이진탐색

T = 테스트 케이스 개수 ( 1 <= T <= 50 )
P, Pa, Pb = 전체 쪽수, A가 찾을 쪽 번호, B가 찾을 쪽 번호
( 1 <= P, Pa, Pb <= 1000 )


예를 들어 책이 총 400쪽이면,
검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고,
중간 페이지 c= int((l+r)/2)로 계산한다.
"""

# 이진 탐색 (계속해서 사용되기 때문에) 함수로 정의
def binary_search(P, finding):
    l = 1  # 왼쪽 끝
    r = P  # 오른쪽 끝
    count = 0  # 탐색 시도한 횟수
    while True:
    # while l <= r:
        # 중간 페이지 get, 탐색 횟수 1증가
        c = int((l + r) / 2)
        count += 1
        # 찾았는지 확인
        # 찾은 경우, 반복 중지
        if c == finding:
            break
        # 못 찾았고, 중간 페이지가 찾는 수보다 크다 -> 오른쪽 끝 값을 c로 변경
        elif c > finding:
            r = c
        # 못 찾았고, 중간 페이지가 찾는 수보다 작다 -> 왼쪽 끝 값을 c로 변경
        else:
            l = c
    # 이진 탐색 횟수 반환
    return count

import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    A = binary_search(P, Pa)
    B = binary_search(P, Pb)
    # A, B 탐색에 걸린 횟수 확인하고 싶으면 출력
    #print(A, B)
    if A > B:
        print(f'#{tc} B')
    elif A < B :
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')