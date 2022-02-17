"""
[파이썬 S/W 문제해결 기본] 3일차
4865 글자수

T = 테스트 케이스
str1 = 길이가 N인 문자열 (5≤N≤100)
str2 = 길이가 M인 문자열 (10≤M≤1000)
(N≤M)

문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
그중 가장 많은 글자의 개수를 출력
파이썬의 경우 딕셔너리를 이용할 수 있다.
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    dct = {}

    # 딕셔너리로 만들기 전에 set 적용해서 중복 제거
    for char in set(str1):
        dct[char] = 0

    # str2의 문자와 비교해서 개수 확인, value값에 저장
    for key in dct.keys():
        for one in str2:
            if key == one:
                dct[key] += 1

    # 가장 큰 값을 출력
    max_num = -1
    for value in dct.values():
        if value > max_num:
            max_num = value
    print(f'#{tc} {max_num}')


