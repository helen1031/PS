import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

cases = list(set(permutations(nums, m)))
cases.sort()
for case in cases:
    print(*case)