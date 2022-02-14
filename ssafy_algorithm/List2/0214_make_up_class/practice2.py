"""
MAP = [['A', 'B', 'G', 'K'], ['T', 'T', 'A', 'B'], ['A', 'C', 'C', 'D']]
3x4 map 배열은 위와 같이 하드코딩하고,
2x2 pattern 배열을 입력받아주세요.
그리고 map 배열에 pattern이라는 패턴 배열이 존재하는지 확인하고
몇 개인지 출력하면 됩니다.

만약, pattern이 존재하고 1개가 발견되었다면 "발견(1개)" 출력
만약, pattern이 없다면 "미발견" 출력

"""

def is_pattern(y, x):
    for i in range(2):
        for j in range(2):
            if MAP[y+i][x+j] != pattern[i][j]:
                return 0
    return 1

MAP = [['A', 'B', 'G', 'K'], ['T', 'T', 'A', 'B'], ['A', 'C', 'C', 'D']]
# pattern = []
# for i in range(2):
#     pattern.append([a for a in input()])
pattern = [list(map(str, input())) for _ in range(2)]

flag = 0
counting = 0
for y in range(len(MAP)-len(pattern)+1):
    for x in range(len(MAP[y])-len(pattern)+1):
        if MAP[y][x] == pattern[0][0]:
            flag = is_pattern(y, x)
            if flag == 1:
                counting += 1

if counting != 0:
    print(f'발견({counting}개)')
else:
    print('미발견')

