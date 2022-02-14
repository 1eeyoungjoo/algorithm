arr=[[3,4,1],[4,5,2],[3,8,3]]

sum = 0
for i in range(len(arr)):
    sum += arr[i][len(arr)-1-i]
print(sum)


Max = 0  # Max = int(-21e8)
for i in range(3):
    sum2 = 0
    for j in range(3):
        sum2 += arr[i][j]
    if Max < sum:
        Max = sum

