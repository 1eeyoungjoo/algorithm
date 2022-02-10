"""
5789 현주의 상자 바꾸기
테스트 케이스의 수 T
상자의 수 N, 숫자 변경 횟수 Q (1 <= N, Q <= 1000)
바꾸고자 하는 숫자 i, L부터 R번 상자까지 값 변경  (1<= L, R <= N)

"""
import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1) :
    N, Q = map(int, input().split())
    arr = [0]*(N+1)
    requested = []

    for i in range(1, Q+1):
        # requested.append([i] + list(map(int, input().split())))
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i

    print(f'#{tc}', end=' ')
    print(*arr)

#     print(f'#{tc}', end=' ')
#     for idx in range(1, len(arr)) :
#         print(f'{arr[idx]}', end=' ')
#     print()
#  언패킹 : list가 numbers일때 print(*numbers)



