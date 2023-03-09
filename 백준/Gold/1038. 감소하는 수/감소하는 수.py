from itertools import combinations

n = int(input())
nums = []
for i in range(1, 11):
    cases = list(combinations(range(0, 10), i))
    for case in cases:
        case = list(case)
        case.sort(reverse=True)
        nums.append(int(''.join(map(str, case))))
        
nums.sort()

try:
    print(nums[n])
except:
    print(-1)
