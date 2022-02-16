import sys
sys.stdin = open('input.txt')

T = int(input())
# 딕셔너리를 활용한 풀이
numbers = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

for tc in range(1, T+1):
    tc, length = input().split()
    string = list(input().split())
    # dat에 사용할 배열
    bucket = [0]*10
    # numbers의 key와 문자가 같은 경우, 해당하는 value == 인덱스의 값 1증가
    for s in string:
        bucket[numbers[s]] += 1

    # numbers의 key, value를 items()로 가져와
    dic = numbers.items()

    print(tc)
    for i in range(10):
        # 각 item 중에서 value와 i 비교
        for j in dic:
            if j[1] == i:
                # key를 bucket에 저장된 수만큼 출력
                print(f'{j[0]} '*bucket[i])
    print()
