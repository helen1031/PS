import sys
input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]
levels.sort()

l = min(levels)
r = l + k
res = 0
while l <= r:
    mid = (l+r) // 2
    tmp = sum([mid - level if mid> level else 0 for level in levels])
    if tmp > k:
        r = mid - 1
    else:
        l = mid + 1
        res = max(mid, res)
        
print(res)