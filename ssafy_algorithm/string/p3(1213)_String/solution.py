import sys
sys.stdin = open('input.txt', encoding='utf-8')

def brute_force(finding, string):
    f = 0
    s = 0
    f_len = len(finding)
    s_len = len(string)
    count = 0
    # 인덱스가 각 길이를 벗어나지 않는 동안
    while s < s_len and f < f_len:
        # 해당 인덱스 값을 비교하여 다른 경우
        if string[s] != finding[f]:
            # s = 기존위치로, f = -1로 변경 (아래에서 1을 더해주기 때문)
            s = s-f
            f = -1
        s = s+1
        f = f+1
        # if문에 걸리지 않고 탐색 완료했다는 건 일치한다는 것
        if f == f_len:
            # 개수를 하나 추가해주고 f를 0으로 초기화
            count += 1
            f = 0
    return count

T = 10
for tc in range(1, T+1):
    tc = int(input())
    finding = input()
    string = input()
    counting = 0
    answer = brute_force(finding, string)
    print(f'#{tc} {answer}')

    # 브루트 포스 아닌 방법(?)
    # 0 1 2 3       len = 4
    # 0 1           len = 2
    for i in range(len(string)-len(finding)+1):
        for j in range(len(finding)):
            if string[i+j] != finding[j]:
                break
        else:
            counting += 1
    print(f'#{tc} {counting}')

