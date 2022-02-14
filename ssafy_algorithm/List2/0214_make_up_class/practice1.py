"""
배열 안에 찾고자 하는 패턴이 있는지 확인하는 문제

arr = [3, 6, 5, 8, 5, 3, 5, 8, 5, 3, 3, 1, 1, 3]
pattern = [3, 5, 8, 5] # 존재하지 않음

arr = [3, 6, 5, 8, 5, 3, 5, 8, 5, 3, 3, 1, 1, 3]
pattern = [3, 5, 8, 5] # 존재함
"""

arr = [3, 6, 5, 8, 5, 3, 5, 8, 5, 3, 3, 1, 1, 3]

pattern = [3, 5, 8, 5] # 존재함

def is_pattern(idx):
    for i in range(len(pattern)):
        if arr[idx+i] != pattern[i]:
            return 0
    return 1

for j in range(len(arr) - len(pattern) + 1):
    ans = is_pattern(j)
    if ans == 1:
        print("존재")
        break
else:
    print("존재하지 않음")