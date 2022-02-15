"""
[파이썬 S/W 문제해결 기본] 2일차
4843 특별한 정렬

T = 테스트 케이스     ( 1<=T<=50 )
N = 정수의 개수       ( 10<=N<=100 )
ai = N개의 정수      ( 1<=ai<=100 )

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로
큰 수와 작은 수를 번갈아 정렬하기
[비고] 10개만 출력
"""
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    original = list(map(int, input().split()))
    new = []
    # 전체 길이 (연산이 자주 돼서 변수로 저장했습니다)
    whole = len(original)

    # 일단 평범하게 정렬
    for i in range(whole-1, 0, -1):
        for j in range(i):
            if original[j] > original[j+1]:
                original[j], original[j+1] = original[j+1], original[j]

    # 정렬 후, 양 끝부터 가운데로 이동하면서 새로운 리스트 new에 추가
    half = whole // 2
    for i in range(half):
        new.append(original[whole-1-i])
        new.append(original[i])

    # 만약 전체 길이가 홀수인 경우, 정중앙의 값이 추가가 안 됐기에 따로 추가해줍니다.
    if whole % 2 == 1:
        new.append(half+1)

    # new의 10개까지만 출력합니다.
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(new[i], end=' ')
    print()

    # <다양한 출력법>
    # result = new[0:10]
    # print(f'#{tc}', end=' ')
    # print(' '.join(map(str, result)))

    # print(f'#{tc} {" ".join(map(str, new[0:10]))}')