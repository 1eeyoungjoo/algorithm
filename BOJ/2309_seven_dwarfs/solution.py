"""
2309 일곱 난쟁이

9C7
"""

import sys

sys.stdin = open('input.txt')
dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

dwarfs.sort()

total = 0
for dwarf in dwarfs:
    total += dwarf

tmp1 = tmp2 = 0
for i in range(9):
    for j in range(i+1, 9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            tmp1 = i
            tmp2 = j
            break


for idx in range(9):
    if idx != tmp1 and idx != tmp2:
        print(dwarfs[idx])



