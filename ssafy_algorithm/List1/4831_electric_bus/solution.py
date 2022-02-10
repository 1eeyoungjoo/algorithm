"""
4831 전기버스
테스트 케이스의 수(노선수) T (1 <= T <= 50)
한 번 충전으로 최대 이동할 수 있는 정류장 수 K, 종점 정류장 N, 충전기가 설치된 정류장 개수 M
(1 <= K, N, M <= 100)
숫자 aj (0 <= aj <= 9)

최소 몇 번 충전을 해야 종점에 도착할 수 있는지 출력
[비고] 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 0을 출력

최소한의 충전
=> 한 번 충전으로 최대 이동할 수 있는 정류장 수 (K) 내에서 가장 멀리 있는, 충전기가 설치된 정류장에서 충전하는 방식

1. 테스크 케이스 수만큼(T) 반복
2. 종점 정류장 N에 도착할 때까지 반복 (while문 사용)
    - while True를 사용하고, 반복 시작할 때마다 N에 도착할 수 있는지 여부 확인, 도착 가능이면 break
    - 현 위치에서 이동 가능 정류장까지 존재하는 충전 가능 정류장 중 가장 큰 숫자 사용.
        - for문으로 충전 가능 정류장 번호가 저장된 리스트 순환하면서 해당하는 정류장 찾기
    - 바뀐 현 위치에서 다시 충전 가능 정류장 탐색
    - 이때, 충전 가능한 정류장이 없다면, 버스 운행이 불가능해지니, 0을 출력하고 끝.
    - 종점에 도착하는 경우, 충전횟수를 반환
    [비고] 출력문 중복 방지를 위해 was_error라는 변수를 사용
"""


import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    # 한 번 충전으로 최대 이동할 수 있는 정류장 수 K, 종점 정류장 N, 충전기가 설치된 정류장 개수 M
    K, N, M = map(int, input().split())
    recharges = list(map(int, input().split()))

    position = count = was_error = 0

    while True:
        # 종료 조건 : 도착했는가
        if position+K >= N:
            break

        # 범위 안에 충전소가 있는가
        # 가장 멀리 있는 충전소를 선택!
        tmp = 0 # 충전소 위치 받을 변수
        for bus_stop in recharges: #[1,3,5,7,9]
            if position < bus_stop <= position+K:
                tmp = bus_stop

        # 없다. 충전소가 없다.
        if tmp == 0:
            was_error = 1
            break
        # 있다면 충전소로 이동!
        else:
            position = tmp
            count += 1

    if was_error:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {count}')
