"""
1859 백만 장자 프로젝트

T = 테스트 케이스의 수
N = 자연수 (2 ≤ N ≤ 1,000,000)
각 날의 매매가를 나타내는 N개의 자연수(공백으로 구분) (10,000이하)


"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    total = 0

    # 검사가 끝난 부분은 잘라내며 진행할 예정
    while len(price) > 1:
        # 최고가와 그 인덱스 변수
        max_pr = -1
        idx = -1
        # 최고가 구하기
        for i in range(len(price)):
            if price[i] > max_pr:
                max_pr = price[i]
                idx = i
        # 인덱스가 0이 아니라면!
        if idx != 0:
            # 판매가 가능하기에 이익을 구해줍니다.
            # 이익 = 최고가 x 인덱스 - 전날의 구매가
            tmp = max_pr * idx # 인덱스 값 = 최고가 전 날수
            for i in range(idx):
                tmp -= price[i]
            total += tmp
        # 첫날부터 최고가 날까지의 문자열 부분 슬라이싱으로 삭제
        price = price[idx+1:]

    print(f'#{tc} {total}')



