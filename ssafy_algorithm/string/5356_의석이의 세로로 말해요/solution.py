"""
5356 의석이의 세로로 말해요

T = 테스트 케이스의 수
다섯 줄
(각 문자열은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’만으로 이루어져 있다.)
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 쪼개지 않고 1차원 배열로 받기
    strings = [input() for i in range(5)]

    # 문자열 중 가장 긴 문자열 길이 구하기
    max_len = 0
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)

    # 출력하기 위해 세로로 읽어서 추가
    new = ''
    for j in range(max_len): # max_len 길이만큼 가로
        for i in range(5): # 5만큼 세로 (세로로 읽어서 안쪽 for문이 세로)
            # 슬라이싱을 이용해 해당 인덱스가 없어도 에러가 나지 않게 처리
            new += strings[i][j:j+1]

    print(f'#{tc} {new}')
