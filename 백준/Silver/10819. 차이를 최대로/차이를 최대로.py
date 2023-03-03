from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
cases = list(permutations(nums, n))

res = 0
for case in cases:
    tmp = 0
    for i in range(1, n):
        tmp += abs(case[i-1]-case[i])
    if tmp > res:
        res = tmp
print(res)