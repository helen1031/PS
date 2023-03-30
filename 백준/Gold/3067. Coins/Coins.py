import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    m = int(input())
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for cost in range(m + 1):
            dp[i][cost] = dp[i-1][cost]
            if cost >= coins[i]:
                dp[i][cost] += dp[i][cost-coins[i]]
                
    print(dp[-1][-1])