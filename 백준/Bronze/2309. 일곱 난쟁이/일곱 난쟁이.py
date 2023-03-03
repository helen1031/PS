from itertools import combinations

import sys
input = sys.stdin.readline

nums = []
for _ in range(9):
    nums.append(int(input()))

cases = list(combinations(nums, 7))
for case in cases:
    if sum(case) == 100:
        case = sorted(case)
        for c in case:
            print(c)
        break
