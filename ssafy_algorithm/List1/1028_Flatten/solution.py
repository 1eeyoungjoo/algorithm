"""
1208 Flatten
평탄화: 최고점과 최저점의 간격을 줄이는 작업
- 평탄화를 모두 수행 시 최고점과 최저점의 차이는 최대 1

가로 길이는 항상 100
첫 번재 줄 - 덤프 횟수 (1이상 1000 이하)
두 번째 줄 - 각 상자의 높이값 (1이상 100 이하)

=> counting sort 응용
"""

import sys

sys.stdin = open('input.txt')
T = 10

for tc in range(1, T+1):
    dump_times = int(input())
    boxes = list(map(int, input().split()))
    bucket = [0]*101 # counting sort에 사용할 배열 정의
    count = 0
    not_finished = 0
    max_num = min_num = 0

    # counting sort
    for box in boxes:
        bucket[box] += 1

    # 덤핑 작업 수행
    while True:
        # 최고점 구하기
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i] != 0:
                max_num = i
                break

        # 최저점 구하기
        for i in range(1, len(bucket)):
            if bucket[i] != 0:
                min_num = i
                break

        # 최고 최저 차이가 1 이하 => 평탄화가 완료됐음을 알 수 있다.
        if max_num - min_num <= 1:
            break
        # 그렇지 않은 경우, 덤프 횟수를 초과하지 않았는지 확인 후 덤핑 진행
        elif count < dump_times:
            bucket[max_num] -= 1
            bucket[max_num-1] += 1
            bucket[min_num] -= 1
            bucket[min_num + 1] += 1
            count += 1
        else:
            break

    print(f'#{tc} {max_num - min_num}')












