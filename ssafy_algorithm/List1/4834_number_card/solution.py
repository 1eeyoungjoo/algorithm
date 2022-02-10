'''
4834 숫자 카드
테스트 케이스의 수 T (1 <= T <= 50)
카드 장수 N (5 <= N <= 100)
숫자 aj (0 <= aj <= 9)

1. 테스크 케이스 수만큼(T) 반복
2. counting sort의 응용
    - 카드 순회하면서 개수를 세어 새로운 배열(bucket)에 저장
3. bucket 배열 내 가장 큰 숫자와 그의 인덱스(카드 숫자)를 출력에 맞게 출력
    - 출력 결과를 보면, 모든 카드 개수가 동일할 때, 맨 끝 숫자 카드를 출력 (#2 8 1)
'''


import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    bucket = [0]*10 # 카드는 0부터 9까지 10장
    for card in cards:
        bucket[card] += 1
    max_card = ['card_num', 0]
    for i in range(len(bucket)):
        if bucket[i] >= max_card[1] :
            max_card[0] = i
            max_card[1] = bucket[i]
    print(f'#{tc} {max_card[0]} {max_card[1]}')

