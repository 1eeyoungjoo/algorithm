"""
1221 GNS
T = 테스트 케이스

가운데 알파벳을 기준으로 비교하게 되면 I만 세 개 (앞이 다른),
나머지는 따로 비교하지 않아도 되는.
=> 다시 보니 그냥 전체를 비교하면 되지 않나 하는 생각이 들어 새로운 풀이 작성.
counting sort 쓰자
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1, T+1):
    tc, length = input().split()
    string = list(input().split())
    # counting sort에 사용할 배열
    count = [0]*10
    # string 내 숫자 문자 순회하면서 비교
    for one in string:
        # 첫 글자가 아닌 가운데 글자를 비교했는데, 첫글자보다 가운데가 겹치는 가짓수가 적기 때문이었습니다.
        # 첫 글자(T, F, S) 가운데 글자 (I)
        # 심지어 I를 기준으로 했을 때 겹치는 FIV, SIX, NIN -> 모두 앞글자가 달라서 무리 없이 가능
        if one[1] == 'I':
            # 가운데 글자가 I인 경우만 따로 분류해서 앞글자 비교
            for idx in (5, 6, 9):
                if one[0] == numbers[idx][0]:
                    count[idx] += 1
        else:
            # 나머지 경우, 가운데 글자를 비교
            for idx in (0, 1, 2, 3, 4, 7, 8):
                if one[1] == numbers[idx][1]:
                    count[idx] += 1

    print(tc)
    for i in range(10):
        for j in range(count[i]):
            print(numbers[i], end=' ')
    print()
