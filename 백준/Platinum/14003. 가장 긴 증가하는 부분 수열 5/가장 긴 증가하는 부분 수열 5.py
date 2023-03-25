import sys
input = sys.stdin.readline

import bisect

n = int(input())
a = list(map(int, input().split()))

dp = [a[0]]
dp_len = [0] * n
for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
        dp_len[i] = len(dp)
    else:
        idx = bisect.bisect_left(dp, a[i])
        dp[idx] = a[i]
        dp_len[i] = idx + 1
    

maxlen = len(dp)
print(maxlen)

ans = []
for i in range(n-1, -1, -1):
    if dp_len[i] == maxlen:
        ans.append(a[i])
        maxlen -= 1
        if maxlen == 0:
            break
print(*ans[::-1])