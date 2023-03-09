import sys
input = sys.stdin.readline

from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for i in range(1, n+1):
    cases = list(combinations(nums, i))
    for case in cases:
        if sum(case) == s:
            ans += 1
print(ans)