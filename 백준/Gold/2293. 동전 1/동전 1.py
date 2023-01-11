import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
coins = []
for _ in range(n):
    c = int(input())
    if c <= k:
        coins.append(c)

for coin in coins:
    dp[coin] += 1
    for tot in range(coin, k+1):
        dp[tot] += dp[tot - coin]
            
print(dp[k])
