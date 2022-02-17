"""
5432 쇠막대기 자르기

T = 테스트 케이스의 수
쇠막대기와 레이저의 배치를 나타내는 괄호표현 (최대 100,000)

 - 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.

 - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.

 - 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.

 - 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()

    idx = 0
    total = 0 # 전체 조각 개수
    counting = 0 # 현재 idx에서의 쇠막대기 개수

    # 인덱스가 문자열 길이를 넘어가지 않는 동안 루프
    while idx < len(string):
        if string[idx] == '(':
            # 붙어있는 괄호'()'는 무조건 레이저를 의미
            if string[idx + 1] == ')':
                # 현재 있는 쇠막대기 개수만큼 조각 생성
                total += counting
                idx += 2
            else: # '('는 새로운 쇠막대기의 등장을 의미
                counting += 1 # 쇠막대기 개수 추가
                idx += 1
        else:  # string[idx] == ')' -> 쇠막대기 하나의 끝을 의미
            counting -= 1 # 쇠막대기 개수 하나 줄어들고
            total += 1 # 레이저가 한 번은 쇠막대를 자르기에 조각 하나 추가
            idx += 1
    print(f'#{tc} {total}')



