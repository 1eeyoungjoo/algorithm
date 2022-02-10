# 상빈님 코드

import sys
sys.stdin = open('input.txt')

ts = int(input())

for i in range(1, ts+1):
    N = int(input())
    cards = list(map(int, input())) #카드목록
    count = [0]*10
    max = 0

    # for j in range(N):  # 카드 목록에서 인덱싱할 번호
    #     for num in range(10):  # 0~9까지의 카드
    #             if cards[j] == num:  # 카드 목록의 수와 0~9까지의 수가 같은 경우
    #                 count[num]+= 1  # count 리스트에 해당 인덱스위치의 숫자가 올라간다.

    for card in cards:
        count[card] += 1

    for lot in count: #카운팅한 카드 개수리스트에서 수를 한개씩 빼서
        if lot >= max : #최대 카드 개수를 찾아 지정한다.
            max = lot
    count.reverse()
    a = count.index(max)  # 최대 카드 개수가 위치한 인덱스(카드숫자) 가져오기
        # 어떻게 역순으로 인덱스 순회하지????;; 큰 수의 카드 번호를 빼오는 법

    for i in range(len(count)-1, -1, -1):
        if max == count[i]:
            max_num = i
            break

    print(f'#{i} {9-a} {max}') #a에서 최고 값을 도출해내는 방법 찾아내기.