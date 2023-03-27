import sys
input = sys.stdin.readline

INF = 10001
n, m = map(int, input().split())
small = set()
for _ in range(m):
    small.add(int(input()))

dp = [[INF] * (int((2 * n) ** 0.5) + 2) for _ in range(n+1)]
dp[1][0] = 0
for i in range(2, n + 1): # i번째 돌
    if i in small:
        continue
    for v in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1
        
ans = min(dp[n])
if ans == INF:
    print(-1)
else:
    print(ans)
        