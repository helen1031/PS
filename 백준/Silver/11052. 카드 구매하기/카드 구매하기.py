n = int(input())
packs = list(map(int, input().split()))

dp = [0] + packs

for i in range(n+1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i-j]+packs[j-1])

print(dp[n])