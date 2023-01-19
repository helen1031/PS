n = int(input())

dp = [[0] * 10 for _ in range(n)]
for i in range(10):
    dp[0][i] = 1
for i in range(n):
    dp[i][0] = 1

for y in range(1, n):
    for x in range(1, 10):
        dp[y][x] = dp[y-1][x] + dp[y][x-1]
        
print(sum(dp[n-1]) % 10007)