"""
[파이썬 S/W 문제해결 기본] 3일차
4864 문자열 비교

T = 테스트 케이스 (1≤T≤50)
str1 = 길이가 N인 문자열
str2 = 길이가 M인 문자열
 (5≤N≤100, 10≤M≤1000, N≤M)
"""

import sys
sys.stdin = open('input.txt')

def is_in(str1, str2):
    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            if str2[i+j] != str1[j]:
                break
        else:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = is_in(str1, str2)
    print(f'#{tc} {result}')